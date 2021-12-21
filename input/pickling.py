"""
Pickling Module 
================
Pickles input into a system object, start_time, and end_time

"""

# import sys
# import os
import pickle
import input.inputprocessor as inputprocessor
import system_factory
# import exciton_diffusion.pythag
# import graphical_out
import cProfile

def __init__():
    pass

def pickling(params):

    """
    Interactive asks the user for an input file, calls the inputprocessor, 
    and return the processed input
    """
    # print(params[0])
    in_file = params[0]
    # out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    
    # rate = 'arrhenius'
    
    my_sys = system_factory.create(system_type, rate, model_type, site_list, dimen)

    pickle_file = pickle_file_name(in_file, 'system')
    pickle_out = open(pickle_file, 'wb')
    pickle.dump(my_sys, pickle_out)
    pickle_out.close()

    pickle_file = pickle_file_name(in_file, 'start_time')
    pickle_out = open(pickle_file, 'wb')
    pickle.dump(start_time, pickle_out)

    pickle_file = pickle_file_name(in_file, 'end_time')
    pickle_out = open(pickle_file, 'wb')
    pickle.dump(end_time, pickle_out)


def pickle_file_name(input_file, object_type):
    pickle_file = input_file -'.txt' + '_' + object_type + '.pickle'

if __name__ == "__main__":
    # cProfile.run('main()','profileout.txt')
    pickling()
