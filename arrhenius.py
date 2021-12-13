"""
Arrhenius method
================

The arrhenius method for calculating the translation probability between two sites.
"""
import prob_rule as p
import system
class Arrhenius(p.ProbRule):
    """
    The Arrhenius class calculates the translation probability, implements the ProbRule interface.
    """
    
    def __init__(self):
        "Empty constructor"
        pass

    def transition_prob(self, site1, site2, system):
        """
        Calculate the transition probability between two sites using the arrhenius method.

        The probability is calcualted using the equation k_12 = v_eff * e^((-1/kb*T)*delta_G - correction_factor)
        
        Reference: https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6
        """
        #p.transition_prob(site1, site2)
        # place holder until implementation
        prob = 1
        return prob
