import sys
import inputprocessor
import system_factory
import model_factory
import model
import system
import site

in_file = sys.argv[1]
out_file = sys.argv[2]

system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
print(site_list)
my_sys = system_factory.create(system_type, site_list, dimen, rate)

my_sys.excite()
print(my_sys.get_excited_site())
my_model = model_factory.create(model_type)

t = start_time

while t < end_time:
    t += my_model.time_step(t, my_sys.get_excited_site(), my_sys) 
