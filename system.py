"""
`System`
==============

This file defines the System class.
"""
from abc import ABC, abstractmethod
import numpy as np
import random
# import graphical_out # remember to reconfigure this


class System(ABC):
    """
    The abstract system class for defining a system of particles.
    """
    @abstractmethod
    def __init__(self, rate, model, site_list, dimen, T = 298):
        """
        Abstract method for creating a system.

        This method should be overloaded.

        :param dimen: the number of dimensions
        :param rate: a ProbRule object
        :param site_list: the list of sites
        :param model: a Model object
        :param T: the temperature
        """
        # dimension of the system
        self.dimen = dimen
        # a probrule object
        self.rate = rate
        # site_list should be a list of sites and their x, y, z coordinates in system
        self.site_list = site_list
        # temperature of system
        self.T = T
        # a model object
        self.model = model

        # List of site positions, required for optimizing get_neighbors
        # remember to move this out of graphical_out
        self.site_list_pos = self.process_sites()

        # List of excited sites POSITIONS,
        self.exc_list = []

        # List of known neighbors. Will map site positions to list of neighbor indices
        self.neighbors_dict = {}

        # a model object
        # self.model = model
        # _exc_sites = []

    def __str__(self):
        """
        Stringify the system, for printing out
        """
        out = []
        for ea_site in self.site_list:
            out.append(str(ea_site))
        return '\n'.join(out)

    def size(self):
        "Returns the size of the system"
        return len(self.site_list)

    # returns an excited site from the system
    def get_excited_sites(self):
        """
        Returns an excited site from the system. 
        :return: returns the first excited site reached
        """

        return self.exc_list

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
        # print("Error: Excited site not found")
        return

    def unexcite(self, site):
        self.exc_list.remove(site)
        site.unexcite()

    def excite(self):
        """
        Excites one randomly chosen site in the system
        """
        rand = int(len(self.site_list) * random.random())
        self.site_list[rand].excited = True
        self.exc_list.append(self.site_list[rand])

    def next_site(self, curr_site):
        """
        Get list of all possible hopping sites

        :param curr_site: the current site
        """
        neighbors = self.get_neighbors(curr_site)

        if len(neighbors) == 0:
            return None
        # calculate coupling rates for each site
        # holds all rates
        couple_lst = []
        for neighbor in neighbors:

            # calculate rate corresponding to this site
            couple = self.rate.transition_prob(curr_site, neighbor, self)
            # appends low side of range to list (ie for site 1, appends 0
            # for site 2, appends rate_1, for site 3, appends rate1 + rate2

            couple_lst.append(couple)
            
        site_next = self.model.select_site(neighbors, couple_lst)

        return site_next

        # should only get here if there are no nearest neighbors
        return None


    def process_neighbors(self, curr_site):
        """
        Get the list of neighbors reachable from the given site.

        :param curr_site: The current site
        """
        # reach is the cutoff distance for looking for nearest neighbors

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


    # Turns a list of sites into a nice numpy array of shape (len(site_list), 3) for processing
    # Params: 
    #           site_list        : a list of sites
    #
    # Returns: A boolean of whether the file/directory exists
    # 
    def process_sites(self):
        if not (isinstance(self.site_list, list)) or (self.site_list is None):
            raise ValueError("Site List must be a non-empty array")

        arr = np.zeros([len(self.site_list),3])

        for i in range(0,len(self.site_list)):
            arr[i,:] = self.site_list[i].get_position()

        return arr

