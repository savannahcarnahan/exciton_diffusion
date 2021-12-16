"""
Crystal
================

"""
import system
import site
import static
class Crystal(static.Static):
    """
    The Crystal class implements a crystal molecule system, where the positions of the molecules are fixed and periodic
    """
    def __init__(self, rate, model, site_list, dimen, T = 298):
        super().__init__(rate, model, site_list, dimen, T)

