"""
Probability Rule
================

"""
from abc import ABC, abstractmethod
import site
class ProbRule(ABC):
    """
    The abstract class for defining transition probabilities between two sites.
    
    """
    @abstractmethod
    def __init__(self):
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
