import model
import kmc
import string
def create(model_type):
    if model_type.lower() == 'kmc':
        return kmc.KMC()
    else:
        raise ValueError(format)


