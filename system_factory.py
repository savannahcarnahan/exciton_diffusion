import crystal
import dynamic
import string
class SystemFactory:
    def create(self, params, format):
        if format.lower() == 'crystal':
            return crystal.Crystal(params)
        elif format.lower() == 'dynamic':
            return dynamic.Dynamic(params)
        else:
            raise ValueError(format)
