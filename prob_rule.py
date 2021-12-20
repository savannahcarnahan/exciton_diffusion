"""
Probability Rule
================

"""
from abc import ABC, abstractmethod
import site
import numpy as np
from numba import jit


class ProbRule(ABC):
    """
    The abstract class for defining transition probabilities between two sites.

    """
    @abstractmethod
    def __init__(self):
        """
        Empty abstract initializer.
        
        """
        pass

    def transition_prob(self, site1, site2):
        """
        The abstract method for calculating the transition probability given two sites.

        :param site1: The first site.
        :param site2: The second site.
        :return: The transition probability.

        """
        if not isinstance(site1, site.Site) or not isinstance(site2, site.Site):
            raise ValueError("Invalid: input must be of type site")

    
    @jit(nopython=True) # Setting nopython = True gives an error I cannot figure out
    def hab_calculator(dipole1, dipole2, R):
        """
        Calculates the coupling between two dipole sites, given their distance vector. This function is accelerated by numba.

        :param site1: The first site containing the dipole
        :param site2: The second site containing the dipole
        :param R: The distance vector between the two sites

        """
        # dipole1 = dipole1.astype(np.float)
        # dipole2 = dipole2.astype(np.float)
        # R = R.astype(np.float)

        epsilon = 8.854e-12 # Unit Fm-1 
        # converting all the vectors to unit vectors
        unit_u1 = dipole1/np.linalg.norm(dipole1)
        unit_u2 = dipole2/np.linalg.norm(dipole2)
        unit_R = R/np.linalg.norm(R)

        # k: Orientation factor
        k = np.dot(unit_u1, unit_u2) - 3*np.dot(unit_u1, unit_R)*np.dot(unit_u2, unit_R)

        # Converting debyee to coulombmeter (SI)
        mag_u1 = np.linalg.norm(dipole1)*3.3356e-30
        mag_u2 = np.linalg.norm(dipole2)*3.3356e-30
        mag_R = np.linalg.norm(R)*1e-10 # Converting angstrom to meters
        hab = (1/(4*np.pi*epsilon))*k*(mag_u1*mag_u2)/(mag_R)**3
        return hab
    
    def dip_dip_hab(self, site1, site2):
        """
        Calculates the coupling between the two sites between two dipole sites.

        :param site1: The first site containing the dipole
        :param site2: The second site containing the dipole

        """

        # Assuming dipole1, dipole2 and R are numpy arrays
        # dipole1: transition dipole of a site1
        # R: distance vector between site1 and site2
        
        dipole1 = getattr(site1, 'dipole').astype(np.float)
        dipole2 = getattr(site2, 'dipole').astype(np.float)
        R = site1.get_position().astype(np.float) - site2.get_position().astype(np.float)

        # print(dipole1)
        # print(dipole2)
        # print(R)

        return ProbRule.hab_calculator(dipole1, dipole2, R)