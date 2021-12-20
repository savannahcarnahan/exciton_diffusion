"""
Model factory 
================

"""
import kmc


def create(model_type):
    """
    | Creates an object of a Model class based on model_type.
    | Currently only **kmc** is supported. Other inputs return an error.

    :param model_type: The type of the model.
    """
    if model_type.lower() == 'kmc':
        return kmc.KMC()
    else:
        raise ValueError(format)
