import numpy as np
import mysite as site
import output.graphical_out as out

def get_diffusion(exc_list, start_site = None):
    if start_site is not None:
        start_pos = start_site.get_position()
    else:
        start_pos = exc_list[0][0].get_position()

    # Generate data of monotonously increasing distances
    d_arr = []
    for i in range(0, len(exc_list)):
        sites_nice = out.process_sites(exc_list[i])
        dist = np.max(np.linalg.norm(sites_nice - start_pos))
        d_arr.append(dist)
    return d_arr

