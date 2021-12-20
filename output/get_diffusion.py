import numpy as np
import mysite as site

def get_diffusion(exc_list):
    diff_dist = []
    diff_dist.append(0)
    start_site = exc_list
    print(start_site)
    pos1 = start_site[0][0].get_position()
    i = 1
    while i<len(exc_list):
        for exc_site in exc_list[i]:
            curr_site = exc_site
            pos2 = curr_site.get_position()
            dist = pos1 - pos2
            dist = np.linalg.norm(dist)
            diff_dist.append(dist)
            i+=1
    # print(diff_dist)
    return diff_dist

