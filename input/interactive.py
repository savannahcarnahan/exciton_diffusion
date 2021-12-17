"""
Interactive Module 
================
Takes a file from interactive input

"""

import sys
import os
import input.inputprocessor
import system_factory
# import exciton_diffusion.pythag
# import graphical_out
import cProfile

def __init__():
    pass

def interactive():

    """
    Interactive asks the user for an input file, calls the inputprocessor, 
    and return the processed input
    """
    in_file = input("What is the name of the input file? ")
    # out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    
    # rate = 'arrhenius'
    
    my_sys = system_factory.create(system_type, rate, model_type, site_list, dimen)
    return my_sys, start_time, end_time

if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    interactive()
