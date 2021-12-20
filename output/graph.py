"""
Graph
=====================

| This generates a graph of exciton diffusion distance over time.
| It takes a set of times and excitation sites as inputs, and
| generates visual output 
|

"""

import numpy as np
import mysite as site
from matplotlib import pyplot as plt
import output.get_diffusion as d


# def graph(t_list, exc_list):
#     fig, ax = plt.subplots( nrows=1, ncols=1 )
#     diff_dist = d.get_diffusion(exc_list)
#     ax.plot(t_list, diff_dist)
#     fig.savefig('diff_dist.png')
#     plt.close(fig)


def graph(t_list, exc_list):
    if not (isinstance(exc_list, list)) or (exc_list is None):
        raise ValueError("Site List must be a non-empty array")
    
    if not (isinstance(t_list, list)) or (t_list is None):
        raise ValueError("Time List must be a non-empty array")

    fig, ax = plt.subplots( nrows=1, ncols=1 )
    diff_dist = d.get_diffusion(exc_list)
    ax.plot(t_list, diff_dist)
    ax.set_xlabel('t')
    ax.set_ylabel('Diffusion Distance')
    fig.savefig('diff_dist.png')
    plt.close(fig)
