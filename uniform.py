"""
Uniform method
================

Returns a uniform number for the coupling; results in uniform probability of choosing 
sites
"""
import prob_rule as p
import system
class Uniform(p.ProbRule):
    """
    The Uniform class calculates the translation probability, implements the ProbRule interface.
    """
    
    def __init__(self):
        "Empty constructor"
        pass

    def transition_prob(self, site1, site2, system):
        """
        Returns a uniform value
        """
        #p.transition_prob(site1, site2)
        # place holder until implementation
        prob = 1
        return prob
