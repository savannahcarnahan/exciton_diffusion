"""
KMC model
============

"""
import model
import numpy as np
class KMC(model.Model):
    """
    The KMC class implements a model.
    """
    def __init__(self):
        self.generator = np.random.default_rng()
        pass

    def time_dist(self,site1, site2, system):
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


