"""
Probability Rule factory
=========================

The class factory for the probability rule class 
"""
import prob_rule
import arrhenius
import marcus
def create(prob_rule_type):
    """
    Creates an object of a `prob_rule` class based on the given type.

    :param prob_rule_type: The type of the probability rule. Currently supported "arrhenius" and "marcus".
    """
    if prob_rule_type.lower() == 'arrhenius':
        return arrhenius.Arrhenius()
    elif prob_rule_type.lower() == 'marcus': # Missed () before
        return marcus.Marcus()
    else:
        raise ValueError(format)


