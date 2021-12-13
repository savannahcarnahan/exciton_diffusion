import atom
import numpy as np
class PointParticle(atom.Atom):

    def __init__(self, *coord):
        self.excited = False
        self.Lambda = 4.8e-20        
        self.dipole = np.array([0, 1, 0])
        self.position = np.asarray(coord)
          
        # should be replaced later maybe?
        # tells function how far away neighbors can be
        self.reach = 10
    
    def __str__(self):
        print(self.position)
        return str(self.position)
  

    def get_position(self):
        return self.position

    
    def transition_probability(system):
        pass

        

