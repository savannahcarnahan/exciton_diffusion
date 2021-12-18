"""
FRET Method
===========

The FRET method for calculating the transition probability between the two sites
"""
import prob_rule as p
import numpy as np
from scipy import constants


class FRET(p.ProbRule):
    """
    The FRET class calculates the translation probability, implements the ProbRule
    interface

    """

    def __init__(self):
        "Empty constructor"
        pass
      
    # Function to calculate spectral overlap
    def spec_overlap(self):
        return 1 

    # calculates the probability with the equation
    # k_12 = 2*pi/hbar * (1/(4*pi*epsilon_0)^2) * Qd *
    #           spec_overlap * J_coul^2
    # see https://pubs.acs.org/doi/full/10.1021/acs.jpcc.1c07929
    def transition_prob(self, site1, site2, system, Qd = 1):
        pi = np.pi
        hbar = constants.hbar
        # Qd = 1 # For most cases Qd = 1
        Jcoul = self.dip_dip_hab(site1, site2)
        SPEC = self.spec_overlap()
        scaling = 10e13
        k_fret = scaling*(2*pi/hbar)*(Jcoul**2)*Qd*SPEC
        return k_fret
