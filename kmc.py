import model
import system
import site
import numpy as np
class KMC(model.Model):
    def __init__(self):
        pass

    def time_dist(self,site1, site2, system):
        couple = system.rate.transition_prob(site1, site2, self)
        my_generator = np.random.default_rng()
        # returns a random time based on an exponential distribution
        # according to couple * exp(-t * couple)
        return np.random.Generator.exponential(my_generator, 1/couple, 1)


    def time_step(self, curr_time, excited_site, system):
        transfer_site = system.next_site(excited_site)
        dt = self.time_dist(transfer_site, excited_site, system)
        setattr(transfer_site, 'is_excited', True)
        setattr(excited_site, 'is_excited', False) 
        return dt
        pass

