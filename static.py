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
    def __init__(self, site_list, dimen, rate):
        super().__init__(site_list, dimen, rate, T = 298)

