from abc import ABC, abstractmethod

class Site(ABC):
    @abstractmethod
    def __init__(self, coords):
        self.position = coords

    @abstractmethod
    def transition_probability():
        pass

    @abstractmethod
    def transition_charge():
        pass

    
    
