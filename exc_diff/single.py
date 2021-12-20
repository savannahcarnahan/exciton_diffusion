"""
Single Module 
================

This propagates an exciton from start time to end time given a system
"""

import sys
import os
import cProfile
def single(system, start_time, end_time):

    """
    Diffuses an exciton in a system from start_time to end_time
    """
    # rate = 'arrhenius'
    
    my_sys = system

    my_sys.excite()
    
    # Need to keep track of excited state and time
    exc_list = []
    t_list = []

    t = start_time
    end_time = 2
    step = 0
    # start_pos = my_sys.get_excited_site().getattr(self, position)
    while t < end_time:
        print('Step', step)
        print('Time', t)
        t_list.append(t)

        exc_site = my_sys.get_excited_sites()
        # print(exc_site.get_position())
        print(exc_site[0])
        exc_list.append(exc_site)
        # print('Site at beginning of time step is ', exc_site)
        # if t == start_time:
            # start_pos = exc_site[0].get_position()
        dt = my_sys.model.time_step(exc_site[0], my_sys)
        if dt == None:
            print("Excited site has no nearest neighbors")
            break
        t += dt
        step += 1

    # end_pos = my_sys.get_excited_sites()[0].get_position()

    # diffusion_dist = pythag.distance(start_pos, end_pos)

    # print(diffusion_dist)
    return t_list, exc_list

def __init__():
    pass


