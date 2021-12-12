from abc import ABC, abstractmethod
import mysite as site
import numpy as np
import ase
class Atom(site.Site):

    def __init__(self, atom_type, *coord):
        self.excited = False
        self.Lambda = 4.8e-20
        self.dipole = np.array([0, 1, 0])
        self.atom = ase.Atom(atom_type, coord)
        self.reach = 3
    
    def excite(self):
        excited = True

    def transition_probability():
        pass
    
    def get_position(self):
        return self.atom.position
    
    def transition_charge():
        pass

    
    
