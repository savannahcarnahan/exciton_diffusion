"""
Com_Line Module 
================
Takes a file from command line input

"""

import sys
import os
import inputprocessor
import system_factory
# import exciton_diffusion.pythag
# import graphical_out
import cProfile

def __init__():
    pass

def command_line(params):

    """
    Interactive asks the user for an input file, calls the inputprocessor, 
    and return the processed input
    """
    print(params[0])
    in_file = params[0]
    # out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    
    # rate = 'arrhenius'
    
    my_sys = system_factory.create(system_type, rate, model_type, site_list, dimen)
    return my_sys, start_time, end_time

if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    command_line()
