"""
KMC model
============

"""
import model
import numpy as np
import random


class KMC(model.Model):
    """
    The KMC class implements a model.
    """
    def __init__(self, seed=None):
        self.generator = np.random.default_rng(seed)
        pass

    def time_dist(self, site1, site2, system):
        """
        Calculates the time distribution.

        :return: a random time based on an exponential distribution, according to couple * exp(-t * couple)
        """
        couple = system.rate.transition_prob(site1, site2, system)
        # returns a random time based on an exponential distribution
        # according to couple * exp(-t * couple)
        return np.random.Generator.exponential(self.generator, 1/couple, 1)[0]

    def time_step(self, excited_site, system): 
        """
        Advance the model by a time step. This method works for one excited site, but
        should be changed if system considers more than one excited site (specifically
        the time step advancement)
        """
        transfer_site = system.next_site(excited_site)
        # print(transfer_site.excited)
        if transfer_site is not None:
            dt = self.time_dist(transfer_site, excited_site, system)
            system.transfer_charge(excited_site, transfer_site)
            # print(transfer_site.excited)
            return dt
        return None

    def select_site(self, site_list, rate_list):
        """
        selects the site based on summing the rates in rate_list and
        choosing a random number between 0 and the sum
        Site is chosen based on where in the range it falls
        If between 0 and k1, return site1, between k1 and k1+k2
        select site2, etc
        """
        if not isinstance(rate_list, list):
            return ValueError('rate_list must be a list')
        last = 0
        rate_ranges = []
        # creates range barriers for rates
        # very important that rate_list is ordered
        for rate in rate_list:
            rate_ranges.append(last)
            last += rate

        rand = last * random.random()
        i = len(rate_ranges)-1

        # selects site based on where the random number falls
        while i >= 0:
            if rate_ranges[i] <= rand:
                return site_list[i]
            i -= 1

        return None
