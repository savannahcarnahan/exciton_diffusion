"""
Run Module
===========

This runs over several exciton runs and either averages the diffusion
distances of all runs or takes the longest run
"""
from exc_diff.single import single
from output.get_diffusion import get_diffusion

def run(system, start_time, end_time, num_runs = 1, diff_calc = 'longest'):
    """
    Runs over several single trajectories
    """
    my_sys = system
    diff_dist = 0

    if diff_calc == 'longest':
        for _ in range(num_runs):
            t_list, exc_list = single(my_sys, start_time, end_time)
            this_dist = get_diffusion(exc_list)[len(exc_list)-1]
            if this_dist > diff_dist:
                diff_dist = this_dist
                ret_exc_list = exc_list
                ret_t_list = t_list
            for site in my_sys.exc_list:
                my_sys.unexcite(site)
    elif diff_calc == 'average':
        for _ in range(num_runs):
            t_list, exc_list = single(my_sys, start_time, end_time)
            this_dist = get_diffusion(exc_list)[len(exc_list)-1]
            diff_dist += 1/num_runs * this_dist
            my_sys.de_excite_site(exc_list[len(exc_list)-1])
            ret_t_list = t_list
            ret_exc_list = exc_list
            for site in my_sys.exc_list:
                my_sys.unexcite(site)

    print('The diffusion distance for this material is', diff_dist)
    return ret_t_list, ret_exc_list

