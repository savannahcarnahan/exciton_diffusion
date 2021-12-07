from abc import ABC, abstractmethod
import numpy as np
import random
import site
import pythag
import random
import prob_rule_factory
import prob_rule
import arrhenius
class System(ABC):

    @abstractmethod
    def __init__(self, site_list, dimen, rate):
        self.dimen = dimen
        # creates an object representing the coupling rate
        self.rate = prob_rule_factory.create(rate)
        # site_list should be a list of sites and their x, y, z coordinates in system
        self.site_list = site_list

    def __str__(self):
        out = []
        for ea_site in self.site_list:
            out.append(str(ea_site))
        return '\n'.join(out)

    def size(self):
        return len(site_list)

    # returns an excited site from the system
    def get_excited_site(self):
        # returns the first excited site reached
        for site in self.site_list:
            if site.excited:
                return site
        return None

    # excites one randomly chosen site in the system
    def excite(self):
        rand = int(len(self.site_list) * random.random())
        self.site_list[rand].excited = True
        

    def next_site(self, curr_site):
        # get list of all possible hopping sites
        # print(curr_site)
        neighbors = self.get_neighbors(curr_site)
        # calculate coupling rates for each site and append current cumulative sum of ranges to list
        # get total of rates
        # holds current cumulative sum
        last = 0
        # holds all previous cumulative sums
        range_lst = []
        for neighbor in neighbors:
            # calculate rate corresponding to this site
            couple = self.rate.transition_prob(curr_site, neighbor)
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
                print('This is the next site', neighbors[i])
                return neighbors[i]
            i -= 1
        # should only get here if there are no nearest neighbors
        return None

    def get_neighbors(self,curr_site):
        # reach is the cutoff distance for looking for nearest neighbors
        reach = getattr(curr_site, 'reach')
        # compile list of possible sites to transfer to
        neighbors = []
        for ea_site in self.site_list:
            dist = pythag.distance(curr_site.get_position(),ea_site.get_position())
            # print(dist)
            if dist > 0 and dist <= reach:
                neighbors.append(ea_site)

        return neighbors
        
        
