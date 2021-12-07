import sys
import inputprocessor
import system_factory
import model_factory
import model
import system
import site
import pythag
in_file = sys.argv[1]
out_file = sys.argv[2]

system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
# print(site_list[0])
my_sys = system_factory.create(system_type, site_list, dimen, rate)

my_sys.excite()
# print(my_sys.get_excited_site())
my_model = model_factory.create(model_type)

t = start_time
# start_pos = my_sys.get_excited_site().getattr(self, position)
while t < end_time:
    exc_site = my_sys.get_excited_site()
    if t == start_time:
        start_pos = getattr(exc_site, 'position')
    t += my_model.time_step(t, exc_site, my_sys)

end_pos = getattr(my_sys.get_excited_site(), 'position')

diffusion_dist = pythag.distance(start_pos, end_pos)

print(diffusion_dist)
