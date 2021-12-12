from abc import ABC, abstractmethod
import mysite as site
import ase
import numpy as np
class Molecule(site.Site):

    def __init__(self, *atom_list):
        self.is_excited = False
        self.molecule = ase.Atoms(atom_list)
    
    def excite(self):
        is_excited = True

    def transition_probability():
        pass
    
    def get_position(self):
        pos = self.molecule.get_positions()
        return np.average(pos, axis = 0)
    
    def transition_charge():
        pass

    
    
