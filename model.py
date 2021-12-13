"""
Model class
================

Define the abstract model class
"""
from abc import ABC, abstractmethod
import site
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
    def time_step():
        """
        The abstract function for advancing one time step
        """
        pass
