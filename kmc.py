import model
import system
import site
class KMC(Model):
    def __init__(self):
        pass

    def time_step(curr_time, excited_site, system):
        transfer_site = system.next_site(curr_site)
        dt = time_step(transfer_site)
        setattr(transfer_site, 'is_excited', True)
        setattr(excited_site, 'is_excited', False) 
        return dt
        pass

