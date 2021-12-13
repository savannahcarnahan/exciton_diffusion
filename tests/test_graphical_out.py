# test_graphical_out.py
# Runs a bunch of tests on the graphics generator
#
#---------------------------------------------------------------------------------------------------
# Imports
#---------------------------------------------------------------------------------------------------
# import os
# import sys
# import inspect

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir) 

import bulktest_generator as gen
import graphical_out
import system_factory
import model_factory
import site_factory

def test_on_random_coordinates(run = 100, particles_per_run = 10, x_limits = [0,5], y_limits  = [0,5], z_limits  = [0,5]):
    for kkkk in range(0,run):
        # Get random values
        system_type = gen.get_system()
        model_type = gen.get_model()
        rate = gen.get_rate()
        # rate = "marcus"
        site_type = gen.get_site()
        site_coord = gen.generate_coordinates(particles_per_run, x_limits = x_limits, y_limits  = y_limits, z_limits  = z_limits)

        # Defined params
        dimen = 3
        start_time = 0
        end_time = 4
        
        site_list = []
        for i in range(0, particles_per_run):
            site_list.append(site_factory.create(site_type, site_coord[i,0], site_coord[i,1], site_coord[i,2]))
        
        # for site in site_list:
        #     print(site)

        my_sys = system_factory.create(system_type, site_list, dimen, rate)
        my_sys.excite()
        my_model = model_factory.create(model_type)

        t = start_time
        end_time = 1 # Add a custom end time to speed things up

        # Need to keep track of excited state and time
        exc_list = []
        t_list = []


        step = 0
        while t < end_time:
            t_list.append(t)

            exc_site = my_sys.get_excited_site()
            exc_list.append([exc_site])

            dt = my_model.time_step(t, exc_site, my_sys)
            
            if dt != 0:
                t += dt
            else:
                break
            step += 1

        # graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None, show = True)

        assert(graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None, show = False))

    pass
    # return (graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None))

# For manual running
def main():
    test_on_random_coordinates(run = 5, particles_per_run=10)
    return

if __name__ == '__main__':
    main()