"""
System factory
================

The class factory for the system class 
"""
import crystal
import dynamic
import string

def create(format, *params):
    """
    Creates an object of a system class based on its format, and pass in the initialization parameters.

    :param format: The name of the system's format. Currently supported "crystal" and "dynamic".
    """
    if format.lower() == 'crystal':
        return crystal.Crystal(*params)
    elif format.lower() == 'dynamic':
        return dynamic.Dynamic(*params)
    else:
        raise ValueError(format)
