"""
Arrhenius method
================

The arrhenius method for calculating the translation probability between two sites.
"""
import prob_rule as p
import numpy as np
from scipy import constants
class Arrhenius(p.ProbRule):
    """
    The Arrhenius class calculates the translation probability, implements the ProbRule interface.
    """
    
    def __init__(self):
        "Empty constructor"
        pass


    # calculates the probability with the equation
    # k_12 = v_eff * e^((-1/kb*T)*delta_G - correction_factor)
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6
    def transition_prob(self, site1, site2, system):      
        T = system.T
        assert isinstance(T, float) or isinstance(T, int)
        kb = constants.Boltzmann
        assert isinstance(kb, float)
        DG = 0 # since molecules are same
        Jcoul = self.dip_dip_hab(site1, site2)
        assert isinstance(Jcoul, float)
        scaling = 10e23
        assert isinstance(scaling, float)
        k_ab = scaling*abs(Jcoul)*np.exp(-(1/kb*T)*DG)
        return k_ab

