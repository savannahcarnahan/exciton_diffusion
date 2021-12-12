import sys
import os
import inputprocessor
import system_factory
import model_factory
import pythag
import graphical_out

in_file = sys.argv[1]
out_file = sys.argv[2]

system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
my_sys = system_factory.create(system_type, site_list, dimen, rate)

print(rate)
print(model_type)

my_sys.excite()
my_model = model_factory.create(model_type)

t = start_time
end_time = 1 # Add a custom end time to speed things up

# Need to keep track of excited state and time
exc_list = []
t_list = []


step = 0
while t < end_time:
    # print('Step', step)
    # print('Time : {0}'.format(t), end = '\r')

    t_list.append(t)

    exc_site = my_sys.get_excited_site()
    exc_list.append([exc_site])

    if t == start_time:
        start_pos = getattr(exc_site, 'position')
    t += my_model.time_step(t, exc_site, my_sys)[0]
    step += 1

    

end_pos = getattr(my_sys.get_excited_site(), 'position')
diffusion_dist = pythag.distance(start_pos, end_pos)

# Save Parameters
save_dir = os.getcwd()
saveparams = [save_dir, "anim_1"]

# graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = saveparams) # This one saves to current working directory
graphical_out.animate_3D(site_list, t_list, exc_list, interval = 100, save_params = None) # This one doesn't save, only plays



