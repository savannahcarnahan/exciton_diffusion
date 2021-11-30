import model
import kmc
import string
class ModelFactory:
    def create(self, params, format):
        if format.lower() == 'kmc':
            return kmc.KMC(params)
        else:
            raise ValueError(format)


