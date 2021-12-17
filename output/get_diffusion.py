import numpy as np
import mysite as site

def get_diffusion(exc_list):
    diff_dist = []
    diff_dist.append(0)
    start_site = exc_list[0]
    pos1 = start_site.get_position()
    i = 1
    while i<len(exc_list):
        curr_site = exc_list[i]
        pos2 = curr_site.get_position()
        dist = pos1 - pos2
        dist = np.linalg.norm(dist)
        diff_dist.append(dist)
        i+=1
    # print(diff_dist)
    return diff_dist

