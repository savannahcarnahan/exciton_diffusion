import numpy as np
import mysite as site
from matplotlib import pyplot as plt
import output.get_diffusion as d

def graph(t_list, exc_list, out_file = 'diff_dist'):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    diff_dist = d.get_diffusion(exc_list)
    ax.plot(t_list, diff_dist)
    fig.savefig(diff_dist + '.png')
    plt.close(fig)

    
