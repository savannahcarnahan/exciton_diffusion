from abc import ABC
import site
class TransitionRule:
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def transition_prob(site1, site2):
        if not isinstance(site1, site.Site) or not isinstance(site2, site.Site):
            raise ValueError("Invalid: input must be of type site")
