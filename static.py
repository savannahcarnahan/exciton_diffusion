"""
Static
================

"""
import system


class Static(system.System):
    """
    The Static class implements a static molecule system, where the positions of the molecules are fixed
    """
    def __init__(self, rate, model, site_list, dimen, T = 298):
        assert isinstance(T, int) or isinstance (T, float)
        super().__init__(rate, model, site_list, dimen,  T)
