"""
Crystal
================

"""
import system
import site
class Crystal(system.System):
    """
    The Crystal class implements a crystal molecule system, where the positions of the molecules are fixed and periodic
    """
    def __init__(self, site_list, dimen, rate):
        super().__init__(site_list, dimen, rate = 'uniform', T = 298)

