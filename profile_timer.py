# A poor man's profiling
# Because numba optimizations are not picked up easily by cProfile

import time
import bulktest_generator as gen
import system_factory
import numpy as np
import pickle
import site_factory
import model_factory

FILENAME = "profiling_vars_1000.pkl"

n_particles = 1000
limits = [0, int(np.sqrt(n_particles))/np.log10(n_particles)]


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
    print("Selected System: {0}".format(system_type))
    model_type = gen.get_model()
    print("Selected Model: {0}".format(model_type))
    rate = gen.get_rate()
    rate = 'marcus'
    print("Selected Rate: {0}".format(rate))
    site_type = gen.get_site()
    print("Selected Site Object: {0}".format(site_type))
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

def generate_and_run_once(inputfile = FILENAME):
    generate_datafile()
    main(inputfile, N = 1)
    return

def main(inputfile, N = 10):
    dimen = 3
    system_type, model_type, rate, site_type, site_coord = import_test_params(inputfile)

    # Generate sites from coordinates
    site_list = []
    for i in range(0, n_particles):
        site_list.append(site_factory.create(site_type, site_coord[i,0], site_coord[i,1], site_coord[i,2]))

    # Generate system
    system = system_factory.create(system_type, site_list, dimen, rate)
    my_model = model_factory.create(model_type)

    total_time = 0
    time_list = []

    # Defined params
    start_time = 0
    end_time = 2

    for i in range(0, N):
        start = time.time()
        system.excite()

        t = start_time
        step = 0

        while t < end_time:
            print('Step', step)
            print('Time', t)
            exc_site = system.get_excited_site()
            
            if t == start_time:
                start_pos = exc_site.get_position()
            t += my_model.time_step(t, exc_site, system)
            step += 1     
        
        end = time.time()

        runtime = end - start
        if (runtime > 8):
            time_list.append(runtime)
            total_time += runtime
    
    print("Number of samples: {0}".format(len(time_list)))
    print("Time List: {0}".format((time_list)))
    print("Average Execution time: " + str((total_time)/(len(time_list))))
    read_model_params(inputfile)
    return 


if __name__ == '__main__':
    main(FILENAME, N = 3)
