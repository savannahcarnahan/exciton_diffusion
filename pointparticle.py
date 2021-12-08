import atom
import numpy as np
class PointParticle(atom.Atom):

    def __init__(self, *coord):
        self.excited = False
        self.Lambda = 0.3 # reorganization energy in eV  
        if not isinstance(coord, np.ndarray):
            self.position = np.asarray(coord)
        else:
            self.position = coord
            print(self.position)
        
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

        

