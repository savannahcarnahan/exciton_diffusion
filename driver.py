import sys
import inputprocessor
import system_factory
import model_factory
import model
import system
import site
import pythag
def main():
    in_file = input("What is the name of the input file? ")
    out_file = input('What is the name of the output file? ')

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
    print(site_list)
    my_sys = system_factory.create(system_type, site_list, dimen, rate)

    my_sys.excite()
    # print(my_sys.get_excited_site())
    my_model = model_factory.create(model_type)

    t = start_time
    step = 0
    # start_pos = my_sys.get_excited_site().getattr(self, position)
    while t < end_time:
        print('Step', step)
        print('Time', t)
        exc_site = my_sys.get_excited_site()
        # print('Site at beginning of time step is ', exc_site)
        if t == start_time:
            start_pos = exc_site.get_position()
        t += my_model.time_step(t, exc_site, my_sys)
        step += 1

    end_pos = my_sys.get_excited_site().get_position()

    diffusion_dist = pythag.distance(start_pos, end_pos)

    print(diffusion_dist)

if __name__ == "__main__":
    main()
