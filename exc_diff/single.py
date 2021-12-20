"""
Single Module 
================

This propagates an exciton from start time to end time given a system
"""

def single(system, start_time, end_time):

    """
    Diffuses an exciton in a system from start_time to end_time
    """
    
    my_sys = system

    my_sys.excite()
    
    # Need to keep track of excited state and time
    exc_list = []
    t_list = []

    t = start_time
    step = 0
    
    while t < end_time:
        print('Time: {0}'.format(t), end = '\r')
        t_list.append(t)

        exc_site = my_sys.get_excited_sites()
        
        exc_list.append(exc_site.copy())
        
        dt = my_sys.model.time_step(exc_site[0], my_sys)
        if dt == None:
            print("Excited site now has no nearest neighbors")
            break
        t += dt
        step += 1

    return t_list, exc_list

def __init__():
    pass


