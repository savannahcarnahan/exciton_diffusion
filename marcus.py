"""
Marcus method
================

The marcus method for calculating the transition probability.
"""

import prob_rule as p
import numpy as np
from numba import jit
from scipy import constants
# import hab
class Marcus(p.ProbRule):
    """
    The Marcus class calculates the transition probability, implementing the ProbRule interface.
    
    Global constants for marcus rate equation
    - :math:`\\overline{h}` = 1.0545e-34
    - :math:`kb` = 1.380e-23
    - :math:`T` = 293

    """
    
    # Global constants for marcus rate equation
    # hbar = 1.0545e-34
    # kb = 1.380e-23
    # T = 293
    
    # creates the correct probability rule
    def __init__(self):
        "Empty constructor."
        pass
    
    # def marcus_rate(self, Hab, Lambda):
    #     k_ab = (2*np.pi/self.hbar)*(np.sqrt(1/(4*np.pi*self.kb*self.T*Lambda))*(Hab**2)*np.exp(-(Lambda/4*self.kb*self.T)))
    #     return k_ab
    # Need H_ab (between site a and b)
    def transition_prob(self, site1, site2, system):
        """
        Calculate the transition probability between two sites using the marcus method.

        The probability is calcualted using the equation k_ab = (2*np.pi/self.hbar)*(np.sqrt(1/(4*np.pi*self.kb*self.T*Lambda))*(Hab**2)*np.exp(-(Lambda/4*self.kb*self.T)))

        :param site1: The first site containing the dipole
        :param site2: The second site containing the dipole
        :param system: The system these particles are in

        :return: $K_{ab}$
        """
        pi = np.pi
        T = system.T
        kb = constants.Boltzmann
        Lambda = site1.Lambda
        hbar = constants.hbar
        Jcoul = self.dip_dip_hab(site1, site2)
        k_ab = 10**-12 * (2*pi/hbar)*(np.sqrt(1/(4*pi*kb*T*Lambda))*(Jcoul**2)*np.exp(-(Lambda/4*kb*T)))
        return k_ab
    
    
