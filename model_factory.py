"""
Model factory 
================

"""
import model
import kmc
import string
def create(model_type):
    """
    Creates an object of a Model class based on its type.

    :param model_type: The type of the model. Currently only "kmc" is supported.
    """
    if model_type.lower() == 'kmc':
        return kmc.KMC()
    else:
        raise ValueError(format)


