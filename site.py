from abc import ABC, abstractmethod

class Site(ABC):

    @abstractmethod
    def transition_probability():
        pass

    @abstractmethod
    def transition_charge():
        pass

    
    
