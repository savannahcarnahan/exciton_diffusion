"""
Uniform Method
==============

Uses the uniform probability method to generate a 'rate'
Not valid for 'real' sites, used for testing
"""
import prob_rule as p


class Uniform(p.ProbRule):
    """
    The Uniform class calculates the transition probability, implements the ProbRule
    interface.
    """

    def __init__(self):
        "Empty constructor"
        pass

    def transition_prob(self, site1, site2, system):

        return 1
