"""
Pythagorean distance
================

"""
import numpy as np

def distance(arr1, arr2):
    """
    Pythagorean (L2) distance between two point positions.

    :param arr1: A numpy array defining the position of the first position.
    :param arr2: A numpy array defining the position of the second position.

    :return: The Pythagorean distance.
    """
    # difference between two arrays
    temp = arr1 - arr2
    # dot product to sum the squares of the coordinates
    sum_sq = np.dot(temp.T, temp)
    # return sqrt
    return np.sqrt(sum_sq)
