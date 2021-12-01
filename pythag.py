import numpy as np

# returns pythagorean distance between two numpy arrays 
# (representing two points)
def distance(arr1, arr2):
    # difference between two arrays
    temp = arr1 - arr2
    # dot product to sum the squares of the coordinates
    sum_sq = np.dot(temp.T, temp)
    # return sqrt
    return np.sqrt(sum_sq)
