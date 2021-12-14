"""
System factory
================

The class factory for the system class 
"""
import crystal
import static
import dynamic
import string
import model_factory
import prob_rule_factory
def create(format, rate, model, *params):
    """
    Creates an object of a system class based on its format, and pass in the initialization parameters.

    :param format: The name of the system's format. Currently supported "crystal" and "dynamic".
    """
    rate = prob_rule_factory.create(rate)
    model = model_factory.create(model)
    
    if format.lower() == 'crystal':
        return crystal.Crystal(rate = rate, model = model, *params)
    if format.lower() == 'static':
        return static.Static(rate = rate, model = model, *params)
    elif format.lower() == 'dynamic':
        return dynamic.Dynamic(rate = rate, model = model, *params)
    else:
        raise ValueError(format)
