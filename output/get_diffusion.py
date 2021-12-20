"""
Get Diffusion
=====================

| This generates a list of diffusion distances
|

"""


import numpy as np
import mysite as site
import output.graphical_out as out

# def get_diffusion(exc_list):
#     diff_dist = []
#     diff_dist.append(0)
#     start_site = exc_list[0]
#     pos1 = start_site.get_position()
#     i = 1
#     while i<len(exc_list):
#         curr_site = exc_list[i]
#         pos2 = curr_site.get_position()
#         dist = pos1 - pos2
#         dist = np.linalg.norm(dist)
#         diff_dist.append(dist)
#         i+=1
#     # print(diff_dist)
#     return diff_dist

def get_diffusion(exc_list, start_site = None):
    if start_site is not None:
        start_pos = start_site.get_position()
    else:
        print(exc_list)
        start_pos = exc_list[0][0].get_position()

    # Generate data of monotonously increasing distances
    d_arr = []
    for i in range(0, len(exc_list)):
        sites_nice = out.process_sites(exc_list[i])
        dist = np.max(np.linalg.norm(sites_nice - start_pos))
        d_arr.append(dist)
    return d_arr

