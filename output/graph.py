import numpy as np
import mysite as site
from matplotlib import pyplot as plt

def graph(t_list, exc_list):
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    diff_dist = [0]
    pos1 = exc_list[0].get_position()
    i = 1
    while i<len(exc_list):
        pos2 = exc_list[i].get_position()
        dist = np.linalg.norm(pos1 - pos2)
        diff_dist.append(diff_dist)
        i+=1

    ax.plot(t_list, diff_dist)
    fig.savefig('diff_dist.png')
    plt.close(fig)

    
