import atom
import numpy as np
class PointParticle(atom.Atom):

    def __init__(self, *coord):
        self.excited = False
        # self.lambda = 0.3        
        self.position = np.asarray(coord)
        
        # should be replaced later maybe?
        # tells function how far away neighbors can be
        self.reach = 3
    
    def __str__(self):
        print(self.position)
        return str(self.position)
  

    def get_position(self):
        return self.position

    
    def transition_probability(system):
        pass

        

