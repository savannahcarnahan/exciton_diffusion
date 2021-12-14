"""
Driver Module 
================

The driver module is the entrypoint of the entire program.
"""

import sys
import os
import inputprocessor
import system_factory
import model_factory
import pythag
import graphical_out
import cProfile
def main():

    """
    The main entry point reads in input/output filenames.
    """
    in_file = input("What is the name of the input file? ")
    # out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    
    # rate = 'arrhenius'
    
    my_sys = system_factory.create(system_type, rate, model_type, site_list, dimen)

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
        exc_list.append([exc_site[0]])
        # print('Site at beginning of time step is ', exc_site)
        if t == start_time:
            start_pos = exc_site[0].get_position()
        dt = my_sys.model.time_step(exc_site[0], my_sys)
        if dt == None:
            print("Excited site has no nearest neighbors")
            break
        t += dt
        step += 1

    end_pos = my_sys.get_excited_sites()[0].get_position()

    diffusion_dist = pythag.distance(start_pos, end_pos)

    print(diffusion_dist)
    save_dir = os.getcwd()
    saveparams = [save_dir, "anim_1"]

    # graphical_out.animate_3D(site_list, t_list, exc_list, interval = 500, padding = 0, save_params = saveparams)  # This one saves to current working directory
    # graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None) # This one doesn't save, only plays

if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    main()
