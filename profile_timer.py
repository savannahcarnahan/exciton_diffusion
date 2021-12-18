# A poor man's profiling

import pythag
import time
import bulktest_generator as gen
import system_factory
import model_factory
import numpy as np
import pickle
import site_factory

FILENAME = "profiling_vars.pkl"

n_particles = 10000
limits = [0, int(np.sqrt(n_particles))]


def import_test_params(filename):
    with open(filename, 'rb') as handle:
        [system_type, model_type, rate, site_type, site_coord] = pickle.load(handle)
    return system_type, model_type, rate, site_type, site_coord

def save_test_params(filename, vars_arr):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(vars_arr, pickle_file)
    return


def generate_test_params():
    # Get random values
    system_type = gen.get_system()
    model_type = gen.get_model()
    rate = gen.get_rate()
    # rate = "marcus"
    site_type = gen.get_site()
    site_coord = gen.generate_coordinates(n_particles, x_limits = limits, y_limits = limits, z_limits = limits)
    return [system_type, model_type, rate, site_type, site_coord]


# Run to generate Test Data
def generate_datafile():
    save_test_params(FILENAME, generate_test_params())
    pass

def read_model_params(inputfile = FILENAME):
    system_type, model_type, rate, site_type, _ = import_test_params(inputfile)
    print("System_Type : {0},          Model_Type = {1}".format(system_type, model_type))
    print("Site_Type   : {0},          Rate       = {1}".format(site_type, rate))
    pass

def main(inputfile, N = 10):
    system_type, model_type, rate, site_type, _ = import_test_params(inputfile)
    site_coord =gen.generate_coordinates(n_particles, x_limits = limits, y_limits  = limits, z_limits  = limits)

    total_time = 0
    time_list = []
    diff_list = []

    # Defined params
    dimen = 3
    start_time = 0
    end_time = 5

    for i in range(0, N):
        start = time.time()

        site_list = []
        for i in range(0, n_particles):
            site_list.append(site_factory.create(site_type, site_coord[i,0], site_coord[i,1], site_coord[i,2]))
        
        # for site in site_list:
        #     print(site)

        my_sys = system_factory.create(system_type, site_list, dimen, rate)
        my_sys.excite()
        my_model = model_factory.create(model_type)

        t = start_time
        end_time = 10 # Add a custom end time to speed things up

        # Need to keep track of excited state and time
        exc_list = []
        t_list = []


        step = 0
        while t < end_time:
            print("t = {0:.5f}".format(t, end = '\r'))
            t_list.append(t)

            exc_site = my_sys.get_excited_site()
            exc_list.append([exc_site])
            
            if t == start_time:
                start_pos = exc_site.get_position()
            
            dt = my_model.time_step(exc_site, my_sys)
            
            if dt != 0:
                t += dt
            else:
                break
            step += 1

        end = time.time()

        diffusion_dist = pythag.distance(start_pos, my_sys.get_excited_site().get_position())

        diff_list.append(diffusion_dist)
        time_list.append(end-start)
        total_time += end-start
    
    print(time_list)
    print("Average Execution time: " + str((total_time)/N))
    read_model_params(inputfile)
    return 


if __name__ == '__main__':
    # generate_datafile() # Run to generate pickle file
    main(FILENAME)
