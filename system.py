from abc import ABC, abstractmethod
import numpy as np
import random
import site
import pythag
import random
import prob_rule_factory
import graphical_out
import prob_rule
import arrhenius
class System(ABC):
    # """
    # The abstract system class for defining a system of particles.
    # """

            
    # Optimization: Maintain dictionary of excited sites neighbors 
    # Optimization: Maintain list of excited sites

    @abstractmethod
    def __init__(self, site_list, dimen, rate):
        # """
        # Abstract method for creating a system.
        # This method should be overloaded.
        # :param dimen: the number of dimensions
        # :param rate: a ProbRule object
        # :param site_list: the list of sites
        # :param model: a Model object
        # :param T: the temperature
        # """
        self.dimen = dimen
        # creates an object representing the coupling rate
        self.rate = prob_rule_factory.create(rate)
        # site_list should be a list of sites and their x, y, z coordinates in system
        self.site_list = site_list

        # List of site positions, required for optimizing get_neighbors
        self.site_list_pos = graphical_out.process_sites(self.site_list)

        # Temperature
        self.T = 298

        # List of excited sites POSITIONS,
        self.exc_list = []

        # List of known neighbors. Will map site positions to list of neighbor indices
        self.neighbors_dict = {}

        # a model object
        # self.model = model
        # _exc_sites = []

    def __str__(self):
        # """
        # Stringify the system, for printing out
        # """
        out = []
        for ea_site in self.site_list:
            out.append(str(ea_site))
        return '\n'.join(out)

    def size(self):
        return len(self.site_list)

    # returns an excited site from the system
    def get_excited_site(self):
        # """
        # Returns an excited site from the system. 
        # :return: returns the first excited site reached
        # """

        return self.exc_list[0]

    def transfer_charge(self, site_old, site_new):
        print("Exc_sites #: " + str(len(self.exc_list)))

        # print(site_old.get_position())

        # for site in self.exc_list:
        #     print(site.get_position())

        self.de_excite_site(site_old)
        self.excite_site(site_new)
        # print("Exc_sites : " + str(len(self.exc_list)))
        pass

    # Excite a site
    def excite_site(self, site):
        setattr(site, 'excited', True)
        self.exc_list.append(site)
        return
    
    # De-excite a site
    def de_excite_site(self, site):
        for exc_site in self.exc_list:
            # print(site.get_position() == exc_site.get_position())            
            if (site.get_position() == exc_site.get_position()).all():
                # remove from exc_list
                # print("Exc_sites : " + str(self.exc_list))
                self.exc_list.remove(exc_site)
                # print("Exc_sites : " + str(self.exc_list))
                setattr(site, 'excited', False)
                return
        print("Error: Excited site not found")
        return


    # excites one randomly chosen site in the system
    def excite(self):
        # "Excites one randomly chosen site in the system"
        rand = int(len(self.site_list) * random.random())
        self.site_list[rand].excited = True
        self.exc_list.append(self.site_list[rand])
        

    def next_site(self, curr_site):
        # """
        # Get list of all possible hopping sites
        # :param curr_site: the current site
        # """

        # get list of all possible hopping sites
        neighbors = self.get_neighbors(curr_site)
        # calculate coupling rates for each site and append current cumulative sum of ranges to list
        # get total of rates
        # holds current cumulative sum
        last = 0
        # holds all previous cumulative sums
        range_lst = []
        for neighbor in neighbors:

            # calculate rate corresponding to this site
            couple = self.rate.transition_prob(curr_site, neighbor, self)
            # appends low side of range to list (ie for site 1, appends 0
            # for site 2, appends rate_1, for site 3, appends rate1 + rate2

            range_lst.append(last)
            last += couple
        # generate random number between 0 and the sum of all the rates
        rand = last * random.random()
        i = len(range_lst)-1
        # selects site based on where in the range the random number falls
        while i >= 0:
            if range_lst[i] <= rand:
                # print('This is the next site', neighbors[i])
                return neighbors[i]
            i -= 1
        # should only get here if there are no nearest neighbors
        return None

    def process_neighbors(self, curr_site):
        reach = getattr(curr_site, 'reach')

        # compile list of possible sites to transfer to       
        distances = (np.linalg.norm(self.site_list_pos - curr_site.get_position(), axis = 1))
        idx = np.where((distances < reach) * (distances != 0))[0]
        return idx

    def return_neighbors(self, idx):
        neighbors = []
        for i in idx:
            neighbors.append(self.site_list[i])

        return neighbors
    
    # Optimized
    def get_neighbors(self,curr_site):
        # """
        # Get the list of neighbors reachable from the given site.
        # :param curr_site: The current site
        # """
        # reach is the cutoff distance for looking for nearest neighbors
        
        # First check if this site has already been processed
        key = str(curr_site.get_position())

        # print("key = " + str(key))
        # print("dict = " + str(self.neighbors_dict))

        if key in self.neighbors_dict:
            idx = self.neighbors_dict[key]
            # print("using dict")
        else:
            # Otherwise find neighbors and add to dict
            idx = self.process_neighbors(curr_site)
            self.neighbors_dict[key] = idx

        return self.return_neighbors(idx)

    
