#---------------------------------------------------------------------------------------------------
# Imports
#---------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import sys
import inputprocessor

#---------------------------------------------------------------------------------------------------
# Global Parameters
#---------------------------------------------------------------------------------------------------

# matplotlib.rcParams['text.usetex'] = True # Want to have this true if printing out LaTeX
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

#---------------------------------------------------------------------------------------------------
# Helpers
#---------------------------------------------------------------------------------------------------

# Make a directory
# Params: 
#           path        : A directory path
#           name        : Name of a file to be created at the directory path; if None, creates a directory by default
#
# Returns: Boolean of success
#
def make_dir(path, name = None):
    import os
    if name is not None:
        dir = path + '//' + name
    else:
        dir = path

    try:
        os.mkdir(dir)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        return False
    else:
        print ("Successfully created the directory %s " % path)
        return True
    


# Find a directory/File
# Params: 
#           path        : A directory path
#           name        : Name of a file to be found at the directory path; if None, returns if directory exists
#
# Returns: A boolean of whether the file/directory exists
# 
def exists_dir(path, name = None):
    import os
    if name is not None:
        return os.path.isdir(path + '//' + name)
    else:
        return os.path.isdir(path)

# Turns a list of sites into a nice numpy array of shape (len(site_list), 3) for processing
# Params: 
#           path        : A directory path
#           name        : Name of a file to be found at the directory path; if None, returns if directory exists
#
# Returns: A boolean of whether the file/directory exists
# 
def process_sites(site_list):
    arr = np.zeros([len(site_list),3])

    for i in range(0,len(site_list)):
        arr[i,:] = site_list[i].position

    return arr



#---------------------------------------------------------------------------------------------------
# Function Libraries
#---------------------------------------------------------------------------------------------------


# Plot sites in a 3D grid
# Params: 
#           site_list   : A list of all sites, of type site object
#           color      : An integer specifying the color
#           alpha       : Opacity Parameter
#
# Returns: True, for now
# 
def plot_sites(site_list, color = 0, alpha = 1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('3D Plot of Sites')

    sites_nice = process_sites(site_list)
    ax.scatter(sites_nice[:,0], sites_nice[:,1], sites_nice[:,2], c = color * np.ones(sites_nice.shape[0]), alpha = alpha)

    plt.show()

    return True


def animate_scatter():
    def update_graph(num):
        data=df[df['time']==num]
        graph._offsets3d = (data.x, data.y, data.z)
        title.set_text('3D Test, time={}'.format(num))


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    title = ax.set_title('3D Test')

    data=df[df['time']==0]
    graph = ax.scatter(data.x, data.y, data.z)

    ani = matplotlib.animation.FuncAnimation(fig, update_graph, 19, 
                                interval=40, blit=False)

    plt.show()

# Excited Sites Animation
# Params: 
#           site_list   : A list of all sites, of type site object
#           t_list      : A list of time-stamps for the animation, of type float
#           exc_list    : A nested list of the excited states for each time t
#           site_rad    : Radius of each site, defaults to 1
#           padding     : Padding between the final site and the edges of animation, of type float/double
#           save_params : An array of two string objects - [save_directory, save_filename], automatically saves if this is not None
#           show        : A boolean of whether to play the animation
#
# Returns: True, for now
# 
def animate_system_2D(site_list, t_list, exc_list, site_rad = 1, save_params = None, padding = 1, show = True):
    print('Animating droplet...')

    # Make directory first if it doesn't exist
    if not (exists_dir(save_params[0])):
        make_dir(save_params[0])

    circles = []
    
    # This is what changes in each frame
    def animate(j):
        for i in range(0, len(R_arr[0])):
            try:
                circles[i].set_radius(R_arr[j][i])
            except:
                print('len(circles), i, j = {2},{0},{1}'.format(i,j, len(circles)))
            
        if (j == len(t_list)):
            plt.close()
        return circles

    # Initializes Frame Data
    def init():
        for site in site_list:
            circles.append(plt.Circle((site[0], center_y[i]), radius=site_rad, fc= colors[i]))
            fig.gca().add_patch(circles[i])
        return circles

    # def init():
    #     for i in range(0, len(center_x)):
    #         circles.append(plt.Circle((center_x[i], center_y[i]), radius=site_rad, fc= colors[i]))
    #         fig.gca().add_patch(circles[i])
    #     return circles

    

    # Set up animation
    rc_arr = config.get_rc()
    center_x = rc_arr[:,0]
    center_y = rc_arr[:,1]
    x_lim = [np.floor(np.min(center_x) - np.max(R_arr[0]) - padding), np.ceil(np.max(center_x) + np.max(R_arr[0]) + padding)]
    y_lim = [np.floor(np.min(center_y) - np.max(R_arr[0]) - padding), np.ceil(np.max(center_y) + np.max(R_arr[0]) + padding)]

    

    fig = plt.figure(figsize=(8,8))
    ax = plt.axes((0.1,0.1,.8,.8))

    # ax.set_xlim(x_lim[0], x_lim[1])
    # ax.set_ylim(y_lim[0], y_lim[1])
    ax.set_xbound(x_lim[0], x_lim[1])
    ax.set_ybound(y_lim[0], y_lim[1])

    ax.set_xticks(np.linspace(x_lim[0], x_lim[1], 3))
    ax.set_yticks(np.linspace(y_lim[0], y_lim[1], 3))

    ax.set_aspect('equal')
    
    # The animation
    animator = ani.FuncAnimation(fig, animate, frames = len(R_arr), interval = 5, init_func = init, repeat = False)
    
    # Save Data if required
    if save_params is not None:
        savepath = save_params[0] + '/' + save_params[1]  + '.mp4'
        animator.save(savepath, fps = 25)
    
    # Play animation if required
    if show:
        plt.show()

    plt.close(fig)

    return True

# Main function just runs a bunch of tests
def main():
    in_file = sys.argv[1]

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)

    # for site in site_list:
    #     print("Site List: {0}".format(site))

    # print("From Process Site Function \n" + str(process_sites(site_list)))

    plot_sites(site_list)

    return


if __name__ == '__main__':
    main()
