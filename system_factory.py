import crystal
import dynamic
import string

def create(format, *params):
    if format.lower() == 'crystal':
        return crystal.Crystal(*params)
    elif format.lower() == 'dynamic':
        return dynamic.Dynamic(*params)
    else:
        raise ValueError(format)
