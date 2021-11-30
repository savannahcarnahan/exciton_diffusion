from abc import ABC, abstractmethod
import site
from ase import Atom
class Atom(site.Site):

    def __init__(self, atom_type, coord):
        self.is_excited = False
        self.atom = Atom(atom_type, coord)

    def transition_probability():
        pass
    
    def position():
        return atom.position
    
    def transition_charge():
        pass

    
    
