"""
Model class
================

Define the abstract model class
"""
from abc import ABC, abstractmethod


class Model(ABC):
    """
    The abstract Model class
    """
    @abstractmethod
    def __init__(self):
        """
        Initialize the Model
        """
        pass

    @abstractmethod
    def time_step(self):
        """
        The abstract function for advancing one time step
        """
        pass
    
    @abstractmethod
    def time_dist(self, site1, site2, system):
        """
        Returns the time for the model to advance
        """
        pass

    @abstractmethod
    def select_site(self, site_list, rate_list):
        """
        Algorithm for selecting site base on coupling rates
        Returns one site
        """
        pass
