import model
import system
import site
import numpy as np
class KMC(Model):
    def __init__(self):
        pass

    def time_dist(site2, site1):
        couple = get_coupling(site1, site2)
        distr = couple * exp


    def time_step(curr_time, excited_site, system):
        transfer_site = system.next_site(curr_site)
        dt = time_dist(transfer_site, curr_site)
        setattr(transfer_site, 'is_excited', True)
        setattr(excited_site, 'is_excited', False) 
        return dt
        pass

