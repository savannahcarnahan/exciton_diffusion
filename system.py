from abc import ABC, abstractmethod
import numpy as np
import random
import site
class System(ABC):
    def __init__(self, site_list, dimen):
        self.dimen = dimen
        # site_list should be a list of sites and their x, y, z coordinates in system
        self.site_list = site_list
    
    def next_site(curr_site):
        # get list of all possible hopping sites
        neighbors = get_neighbors(curr_site)
        # calculate coupling rates for each site and append ranges to list
        # get total of rates
        last = 0
        range_lst = []
        for neighbor in neighbors:
            couple = get_coupling(curr_site, neighbor)
            range_lst.append(last)
            last += couple
        rand = last * random.random()
        i = len(range_lst)-1
        while i >= 0:
            if range_lst[i] <= rand:
                return neighbors[i]
            i -= 1
        # should only get here if there are no nearest neighbors
        return None

    def get_neighbors(curr_site):
        # reach is the cutoff distance for looking for nearest neighbors
        reach = getattr(curr_site, 'reach')
        
        
