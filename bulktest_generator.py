# test_bulk.py
# Generates a series of test input in bulk for specified parameters
# -------------------------------------------------------------------------------------
import numpy as np

RATES = ["arrhenius", "marcus","fret"]
SYSTEMS = ["crystal"]
MODELS = ["kmc"]
# SITES = ["atom", "pointparticle"]
SITES = ["pointparticle"]

# Generates coordinates at random from given limits
# Params: 
#           num         : Number of coordinates to sample
#           x_limits    : A list of [lower_bound, upper_bound] for x, where lower_bound < upper bound and both are integers
#           y_limits    : A list of [lower_bound, upper_bound] for y, where lower_bound < upper bound and both are integers
#           z_limits    : A list of [lower_bound, upper_bound] for z, where lower_bound < upper bound and both are integers
#
# Returns: True, for now
#
def generate_coordinates(num, x_limits = [0,2], y_limits  = [0,2], z_limits  = [0,2]):
    if (not (isinstance(num, int)) or (num is None)) or not(num > 0):
        raise ValueError("num must be a positive integer") 

    if (not (isinstance(x_limits, list)) or (x_limits is None)) or ((not len(x_limits) == 2) or (not x_limits[0] < x_limits[1])):
        raise ValueError("x_limits must be an array of length 2, with x_limits[0] < x_limits[1]") 

    if (not (isinstance(y_limits, list)) or (y_limits is None)) or ((not len(y_limits) == 2)or (not y_limits[0] < y_limits[1])):
        raise ValueError("y_limits must be an array of length 2, with y_limits[0] < y_limits[1]") 
    
    if (not (isinstance(z_limits, list)) or (z_limits is None)) or ((not len(z_limits) == 2) or (not z_limits[0] < z_limits[1])):
        raise ValueError("z_limits must be an array of length 2, with z_limits[0] < z_limits[1]") 

    ret = np.zeros([num, 3])

    ret[:, 0] = np.random.randint(x_limits[0],high=x_limits[1], size=num)
    ret[:, 1] = np.random.randint(y_limits[0],high=y_limits[1], size=num)
    ret[:, 2] = np.random.randint(z_limits[0],high=z_limits[1], size=num)
    
    return ret

# Get random rate from RATES array
def get_rate():
    return np.random.choice(RATES)

# Get random system from SYSTEMS array
def get_system():
    return np.random.choice(SYSTEMS)

# Get random model from MODELS array
def get_model():
    return np.random.choice(MODELS)

# Get random site from SITES array
def get_site():
    return np.random.choice(SITES)


def main():
    print(generate_coordinates(2, x_limits = [-10, 10]))
    print(get_rate())
    print(get_system())
    print(get_model())
    return


if __name__ == '__main__':
    main()