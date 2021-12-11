from abc import ABC, abstractmethod
import mysite as site
import ase
import atom
import numpy as np

class Molecule(site.Site):

    def __init__(self, *atom_list):
        # atom_list should be a list of ase.Atom objects
        self.is_excited = False
        self.atom_list = atom_list
        print(atom_list)
        self.num_atom = len(self.atom_list)
        self.molec = ase.Atoms(symbols = atom_list)
    
    def excite(self):
        is_excited = True

    def transition_probability():
        pass
    
    def get_position(self):
        pos = self.molec.get_positions()
        return pos.average(x, axis=0)
    
    def transition_charge():
        pass

    
    
