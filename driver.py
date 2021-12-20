"""
Driver Module 
================

The driver module is the entrypoint of the entire program.
"""

import sys
import os
import input.com_line as i
import exc_diff.run as ex
import output.graphical_out as graphical_out
import output.graph as graph


def main():

    """
    The main entry point reads in input/output filenames.
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
