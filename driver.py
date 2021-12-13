import sys
import os
import inputprocessor
import system_factory
import model_factory
import pythag
import graphical_out
def main():
    in_file = input("What is the name of the input file? ")
    out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    print(site_list)
    my_sys = system_factory.create(system_type, site_list, dimen, rate)

    my_sys.excite()
    # print(my_sys.get_excited_site())
    my_model = model_factory.create(model_type)
    
    # Need to keep track of excited state and time
    exc_list = []
    t_list = []

    t = start_time
    step = 0
    # start_pos = my_sys.get_excited_site().getattr(self, position)
    while t < end_time:
        print('Step', step)
        print('Time', t)
        t_list.append(t)

        exc_site = my_sys.get_excited_site()
        exc_list.append([exc_site])
        # print('Site at beginning of time step is ', exc_site)
        if t == start_time:
            start_pos = exc_site.get_position()
        t += my_model.time_step(t, exc_site, my_sys)
        step += 1

    end_pos = my_sys.get_excited_site().get_position()

    diffusion_dist = pythag.distance(start_pos, end_pos)

    print(diffusion_dist)
    save_dir = os.getcwd()
    saveparams = [save_dir, "anim_1"]

    graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = saveparams) 
    # This one saves to current working directory
    # graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None) 
    # This one doesn't save, only plays

if __name__ == "__main__":
    main()
