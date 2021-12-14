"""
Static
================

"""
import system
import site
class Static(system.System):
    """
    The Static class implements a static molecule system, where the positions of the molecules are fixed
    """
    def __init__(self, rate, model, site_list, dimen, T = 298):
        super().__init__(rate, model, site_list, dimen,  T)

