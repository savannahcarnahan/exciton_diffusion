"""
System Factory
================

The class factory for the system class 
"""
import crystal
import static
import dynamic
import model_factory
import prob_rule_factory


def create(format, rate, model, *params):
    """
    Creates an object of a system class based on its format, and pass in the initialization parameters.

    :param format: The name of the system's format. Currently supported "static", "crystal" and "dynamic".
    """
    rate = prob_rule_factory.create(rate)
    model = model_factory.create(model)
    site_list = params[0]
    dimen = params[1]
    adds = []
    if len(params) >= 3:
        T = params[2]
        adds.append(T)
    if format.lower() == 'crystal':
        return crystal.Crystal(rate, model, site_list, dimen, *adds)
    if format.lower() == 'static':
        return static.Static(rate, model, site_list, dimen, *adds)
    elif format.lower() == 'dynamic':
        return dynamic.Dynamic(rate, model, site_list, dimen, *adds)
    else:
        raise ValueError(format)
