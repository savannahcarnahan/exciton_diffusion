from abc import ABC, abstractmethod
import mysite as site
import ase
class Molecule(site.Site):

    def __init__(self, *atom_list):
        self.is_excited = False
        self.molecule = ase.Atoms(symbols = atom_list)
    
    def excite(self):
        is_excited = True

    def transition_probability():
        pass
    
    def get_position(self):
        return self.atom.position
    
    def transition_charge():
        pass

    
    
