"""
Graphical Out
================

Plotting graphical outputs given a simulation output file.
"""
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from mpl_toolkits.mplot3d import Axes3D
import sys
import input.inputprocessor as inputprocessor

#---------------------------------------------------------------------------------------------------
# Global Parameters
#---------------------------------------------------------------------------------------------------

# matplotlib.rcParams['text.usetex'] = True # Want to have this true if printing out LaTeX
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'

COLORS =  ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

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
    """
    Helper functoin to make a new directory
    """
    # Ensure proper inputs
    if not (isinstance(path, str)) or not (isinstance(name, str)):
        raise TypeError("Arguments must be string")
    
    if (path is None):
        raise ValueError("Path must be specified")

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
    # Ensure proper inputs
    if not (isinstance(path, str)):
        raise TypeError("Arguments must be string")
    
    if (path is None):
        raise ValueError("Path must be specified")

    if name is not None:
        if not (isinstance(name, str)):
            raise TypeError("Filename must be string")
        return os.path.isdir(path + '//' + name)
    else:
        return os.path.isdir(path)

# Turns a list of sites into a nice numpy array of shape (len(site_list), 3) for processing
# Params: 
#           site_list        : a list of sites
#
# Returns: A boolean of whether the file/directory exists
# 
def process_sites(site_list):
    if not (isinstance(site_list, list)) or (site_list is None):
        raise ValueError("Site List must be a non-empty array")

    arr = np.zeros([len(site_list),3])

    for i in range(0,len(site_list)):
        arr[i,:] = site_list[i].get_position()

    return arr


# Finds the entry of a site in a list of sites
# Params: 
#           site_list   : A 2D array of site positions
#           site        : The site position to be found in the site_list array
#
# Returns: The index of site in site_list
# 
def find_site(site_list, site):
    if not (isinstance(site_list, (np.ndarray, np.generic))) or (site_list is None):
        raise ValueError("Site List must be a non-empty numpy array")    

    for i in range(0, site_list.shape[0]):
        if (site == site_list[i]).all():
            return i
    return


#---------------------------------------------------------------------------------------------------
# Function Libraries
#---------------------------------------------------------------------------------------------------


# Plot sites in a 3D grid
# Params: 
#           site_list   : A list of all sites, of type site object
#           color       : An integer specifying the color
#           alpha       : Opacity Parameter
#
# Returns: True, for now
# 
def plot_sites(site_list, exc_list = None, color = COLORS[0], alpha = 1):
    if not (isinstance(site_list, list)) or (site_list is None):
        raise ValueError("Site List must be a non-empty array")
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('3D Plot of Sites')

    sites_nice = process_sites(site_list)
    ax.scatter(sites_nice[:,0], sites_nice[:,1], sites_nice[:,2], c = color, alpha = alpha)

    if exc_list is not None:
        sites_nice = process_sites(exc_list)
        ax.scatter(sites_nice[:,0], sites_nice[:,1], sites_nice[:,2], c = COLORS[3], alpha = alpha)

    plt.show()

    return True

# Plot diffusion distance
def plot_diff_dist(start_site, t_list, exc_list, alpha = 1):
    if not (isinstance(exc_list, list)) or (exc_list is None):
        raise ValueError("Site List must be a non-empty array")
    
    start_pos = start_site.get_position()

    # Generate data of monotonously increasing distances
    dmax_outer = -1
    d_arr = []
    t_arr = []
    for i in range(1, len(exc_list)):
        sites_nice = process_sites(exc_list[i])
        dist = np.max(np.linalg.norm(sites_nice- start_pos))
        # print(dist)
        if dist > dmax_outer:
            dmax_outer = dist
            d_arr.append(dist)
            t_arr.append(t_list[i])

    plt.figure()
    plt.plot(t_arr, d_arr)
    plt.xlabel('t')
    plt.ylabel('Diffusion distance')

    plt.show()

    return True


# Excited Sites Animation
# Params: 
#           site_list   : A list of all sites, of type site object
#           t_list      : A list of time-stamps for the animation, of type float
#           exc_list    : A nested list of the excited sites for each time t
#           save_params : An array of two string objects - [save_directory, save_filename], automatically saves if this is not None
#           site_rad    : Radius of each site, defaults to 100
#           interval    : Interval between subsequent frames - higher value slows down the animation
#           padding     : Padding between the final site and the edges of animation, of type float/double
#           show        : A boolean of whether to play the animation
#           repeat      : A boolean of whether or not to repeat the animation once it finishes playing
#
# Returns: True, for now
# 
def animate_3D(site_list, t_list, exc_list, save_params = None, site_rad = 100, interval = 100, padding = 1, show = True, repeat = True):
    if not (isinstance(site_list, list)) or (site_list is None):
        raise ValueError("Site List must be a non-empty list")
    
    if not (isinstance(t_list, list)) or (t_list is None):
        raise ValueError("t List must be a non-empty list") 
    
    if (not (isinstance(exc_list, list)) or (not (len(exc_list) == len(t_list)) or (exc_list is None))):
        raise ValueError("exc_list must be an nested list of sites whose dimensions must match t_list")  
    
    if (not (site_rad > 0) or not (interval > 0)) or (not (padding >= 0)):
        raise ValueError("site_rad and interval must all be positive integers, while padding must be non-negative")
    
    if (not (isinstance(site_rad, int)) or not (isinstance(interval, int))) or (not (isinstance(padding, int))):
        raise TypeError("site_rad, padding and interval must all be integers")
    
    # print('Animating droplet...')

    # This is what changes in each frame
    def animate(j):
        title.set_text('3D Animation Of Site Excitations, time={0:.5f}'.format(t_list[j]))
        exc_sites = exc_list[j]

        # use colors 0 and 3 -> 0 for blue, 3 for red
        colors = np.array([COLORS[0]] * sites_nice.shape[0])
        
        for site in exc_sites:
            i = find_site(sites_nice, site.position)
            colors[i] = COLORS[3]
    
        scat3D.set_color(colors)


    # Set up animation
    sites_nice = process_sites(site_list)

    fig = plt.figure(figsize=(8,8))
    ax3d = fig.add_subplot(111, projection='3d')

    # ax3d = Axes3D(fig, auto_add_to_figure=False)
    # fig.add_axes(ax3d)
    scat3D = ax3d.scatter(sites_nice[:,0], sites_nice[:,1], sites_nice[:,2], s=site_rad)
    title = ax3d.text2D(0.05, 0.95, "", transform=ax3d.transAxes)

    # Set Anim parameters
    x_lim = [np.min(sites_nice[:,0])-padding, np.max(sites_nice[:,0])+padding]
    y_lim = [np.min(sites_nice[:,1])-padding, np.max(sites_nice[:,1])+padding]
    z_lim = [np.min(sites_nice[:,2])-padding, np.max(sites_nice[:,2])+padding]

    ax3d.set_xlim3d(x_lim[0], x_lim[1])
    ax3d.set_ylim3d(y_lim[0], y_lim[1])
    ax3d.set_zlim3d(z_lim[0], z_lim[1])

    ax3d.set_xticks(np.linspace(x_lim[0], x_lim[1], 3))
    ax3d.set_yticks(np.linspace(y_lim[0], y_lim[1], 3))
    ax3d.set_zticks(np.linspace(z_lim[0], z_lim[1], 3))
    
    # The animation
    animator = ani.FuncAnimation(fig, animate, frames = len(t_list), interval = interval, repeat = repeat, repeat_delay = 1000, blit = False)
    # anim = ani.FuncAnimation(fig, update_graph, 19, interval=40, blit=False)

    # Save Data if required
    if save_params is not None:
        print("Saving animation...")
        # Make directory first if it doesn't exist
        if not (exists_dir(save_params[0])):
            make_dir(save_params[0])

        savepath = save_params[0] + '/' + save_params[1]  + '.mp4'
        animator.save(savepath, fps = 125)
    
    # Play animation if required
    if show:
        plt.show()

    plt.close(fig)

    return True

# Main function just runs a bunch of tests
def main():
    import exc_diff.single as ex

    in_file = sys.argv[1]

    system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)

    t_list, exc_list = ex.single(system_type, start_time, end_time)



    # animate_3D(site_list, np.ones(3000), [], save_params = None)

    return


if __name__ == '__main__':
    main()
