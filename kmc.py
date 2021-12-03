import model
import system
import site
import numpy as np
class KMC(model.Model):
    def __init__(self):
        pass

    def time_dist(site1, site2, system):
        couple = system.get_coupling(site1, site2)
        # returns a random time based on an exponential distribution
        # according to couple * exp(-t * couple)
        return np.random.Generator.exponential(1/couple, 1)


    def time_step(curr_time, excited_site, system):
        transfer_site = system.next_site(curr_site)
        dt = time_dist(transfer_site, curr_site, system)
        setattr(transfer_site, 'is_excited', True)
        setattr(excited_site, 'is_excited', False) 
        return dt
        pass

