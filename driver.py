"""
Driver Module 
================

| The driver module contains code for lauching all the other functions
| of the exciton diffusion simulation. It can be modified or customized
| to extend functionality of the program.
"""

import sys
import os
import input.com_line as i
import exc_diff.run as ex
import output.graphical_out as graphical_out
import output.graph as graph


def main():

    """
    | The **main()** module is the entry point for the program.
    | It organizes and coordinates the execution of the other modules:
    | - Reads in command line arguments and sends to the arg parser.
    | - Launches a simulation, currently for a single point, through
    |   the call to **exc_diff.single()**. This is currently a single point
    |   simulation and will be extended later for multiple particles.
    | - Sets the save path and feeds simulation results to an output module.
    """
    
    system, start_time, end_time = i.command_line(sys.argv[1:])

    t_list, exc_list = ex.run(system, start_time, end_time, 10)

    save_dir = os.getcwd()
    saveparams = [save_dir, "anim_1"]

    # csv.write_csv(t_list, exc_list, name ="kipp_bug")

    # graph.graph(t_list, exc_list)

    # graphical_out.plot_diff_dist(system.site_list[0], t_list, exc_list)

    # graphical_out.animate_3D(system.site_list, t_list, exc_list, interval = 500, padding = 0, save_params = saveparams)



    # This one saves to current working directory
    graphical_out.animate_3D(system.site_list, t_list, exc_list, interval = 100, save_params = None)
    # This one doesn't save, only plays


if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    main()
