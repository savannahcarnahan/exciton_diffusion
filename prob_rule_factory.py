"""
Probability Rule factory
=========================

The class factory for the probability rule class 
"""
import prob_rule
import arrhenius
import marcus
import uniform
def create(prob_rule_type):
    """
    Creates an object of a `prob_rule` class based on the given type.

    :param prob_rule_type: The type of the probability rule. Currently supported "arrhenius", "uniform", and "marcus".
    """
    if prob_rule_type.lower() == 'arrhenius':
        return arrhenius.Arrhenius()
    elif prob_rule_type.lower() == 'marcus': # Missed () before
        return marcus.Marcus()
    elif prob_rule_type.lower() == 'uniform':
        return uniform.Uniform()
    else:
        raise ValueError(format)


