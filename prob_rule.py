from abc import ABC, abstractmethod
import site
class ProbRule(ABC):
    @abstractmethod
    def __init__(self):
        pass

    
    def transition_prob(self, site1, site2):
        if not isinstance(site1, site.Site) or not isinstance(site2, site.Site):
            raise ValueError("Invalid: input must be of type site")
