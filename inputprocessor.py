import sys
import string
#import mysite as site
import site_factory
import ase
import numpy as np
def process_input(in_file):
    in_file = open(in_file)
    conditions = in_file.readline()
    conditions = conditions.split()
    system_type = conditions[0]
    dimen = int(conditions[1])
    rate = conditions[2]
    model_type = conditions[3]
    start_time = float(conditions[4])
    end_time = float(conditions[5])
    
    site_list = []
    molecule = False
    lines = (line.rstrip() for line in in_file)
    lines = (line for line in lines if line) 
    for line in lines:
        params = line.split()
        if params[0].lower() != 'molecule' and not molecule:
            for i,s in enumerate(params):
                if is_float(s):
                    params[i] = float(s)
            site_list.append(site_factory.create(*params))
        elif params[0].lower() == 'molecule' and molecule:
            print(molec)
            site_list.append(site_factory.create('molecule', *molec))
            molec = []
        elif params[0].lower() == 'molecule' and not molecule:
            molecule = True
            molec = []
        elif molecule:
            coord = []
            for i,s in enumerate(params):
                if is_float(s):
                    coord.append(float(s))
            molec.append(ase.Atom(params[0], np.array(coord)))

        
#    for site in site_list:
#        print(site)
    return system_type, site_list, dimen, rate, model_type, start_time, end_time


def is_float(string):
    try:
        float(string)
    except ValueError:
        return False
    return True
