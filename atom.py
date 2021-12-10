from abc import ABC, abstractmethod
import mysite as site
import ase
class Atom(site.Site):

    def __init__(self, atom_type, *coord):
        self.is_excited = False
        self.atom = ase.Atom(atom_type, coord)
    
    def excite(self):
        is_excited = True

    def transition_probability():
        pass
    
    def get_position(self):
        return self.atom.position
    
    def transition_charge():
        pass

    
    
