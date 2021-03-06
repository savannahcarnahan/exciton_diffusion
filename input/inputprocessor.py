"""
Input Processor
================

Parse an input file for a simulation configuration, which includes the types of system, model, etc., as well as a list of positions.

TODO: An example of the input file format.
"""
# import sys
# import string
# import mysite as site
import site_factory
import ase
import numpy as np
def process_input(in_file):
    """
    Process a single input file.

    :param in_file: the filename of the input file.
    """
    in_file = open(in_file)
    conditions = in_file.readline()
    conditions = conditions.split()
    system_type = conditions[0]
    dimen = int(conditions[1])
    rate = conditions[2]
    model_type = conditions[3]
    start_time = float(conditions[4])
    end_time = float(conditions[5])
    molec = []    
    site_list = []
    molecule = False
    lines = (line.rstrip() for line in in_file)
    lines = (line for line in lines if line) 
    for line in lines:
        params = line.split()
        #first if is for atom and point particle processing
        if params[0].lower() != 'molecule' and not molecule:
            for i,s in enumerate(params):
                if is_float(s):
                    params[i] = float(s)
            site_list.append(site_factory.create(*params))
        # makes a molecule and sets up for the next molecule
        elif params[0].lower() == 'molecule' and molecule:
            site_list.append(site_factory.create('molecule', *molec))
            molec = []
        # switches the molecule switch on
        elif params[0].lower() == 'molecule' and not molecule:
            molecule = True
            molec = []
        # adds an ase Atom to a molecule
        elif molecule:
            coord = []
            for i,s in enumerate(params):
                if is_float(s):
                    coord.append(float(s))
            molec.append(ase.Atom(params[0], np.array(coord)))
    # adds molec to site_list if it exists and is not empty
    if ('molec' in locals()) and len(molec)!=0:
        site_list.append(site_factory.create('molecule', *molec))
#    for site in site_list:
#        print(site)
    return system_type, site_list, dimen, rate, model_type, start_time, end_time


def is_float(string):
    """
    Check if a string contains a floating point number.
    
    :param string: The given string.
    :return: True if the string contains a floating point number
    """
    try:
        float(string)
    except ValueError:
        return False
    return True
