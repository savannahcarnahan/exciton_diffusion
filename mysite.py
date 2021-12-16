"""
Site 
================

The abstract definition of a site.
"""
from abc import ABC, abstractmethod

class Site(ABC):
    """
    The abstract class defining a Site.
    """
    @abstractmethod
    def __init__(self, *coords):
        """
        The Site should be initialized with its coordinates.
        :param coords: initial coordinates.
        """
        self.position = coords
        

    @abstractmethod
    def get_position(self):
        "Get the position of this site."
        return self.position

    
    
