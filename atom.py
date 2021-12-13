"""
Atoms
================

"""
from abc import ABC, abstractmethod
import mysite as site
import numpy as np
import ase
class Atom(site.Site):
    """
    The Atom class implements a single atom, with its given type and a position.
    """
    def __init__(self, atom_type, *coord):
        """
        Initialize an atom.

        :param atom_type: The aton's type.
        :param coord: The coordinates of the atom.
        """
        self.excited = False
        self.Lambda = 4.8e-20
        self.dipole = np.array([0, 1, 0])
        self.atom = ase.Atom(atom_type, coord)
        self.reach = 3
    
    def excite(self):
        """
        Set the atom to be excited.
        """
        excited = True

    def transition_probability():
        """
        Calculate the transition probability of this atom.
        """
        pass
    
    def get_position(self):
        """
        Get the position of this atom.

        :return: The position of atom.
        """
        return self.atom.position
    
    def transition_charge():
        """
        Calculate the transition charge of this atom.
        """
        pass

    
    
