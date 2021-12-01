import atom
import numpy as np
class PointParticle(atom.Atom):

    def __init__(self, coord):
        self.is_excited_ = False
        self.position = coord
        self.reach = 3
    
    def __str__(self):
        return np.array2string(self.position)
    
    def get_position(self):
        return self.position
    
    def transition_probability(system):
        pass

        

