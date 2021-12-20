"""
Dynamic system
================

"""
import system


class Dynamic(system.System):
    """
    | The class Dynamic defines a dynamic particles system, where molecules
    | can move freely in space.
    | This class is passed a System object containing the following:
    | - Rate: this object is the probability rule
    | - Model: this object is used to calculate time steps (currently KMC)
    | - Site list: this is a collection of site objects
    | - Dimension: this is the number of physical dimensions to simulate
    | - Temperature: simulation temperature in Kelvin
    """
    pass
