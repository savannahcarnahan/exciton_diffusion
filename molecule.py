"""
Molecule
================

The molecule class implements a site
"""
import mysite as site
import ase
import numpy as np


class Molecule(site.Site):
    """
    The Molecule class
    """
    def __init__(self, *atom_list):
        """
        Initialize a Molecule class.

        :param atom_list: The list of atoms in the molecule.

        The reach between atoms is guesstimated in Angstroms. See https://pubs.acs.org/doi/full/10.1021/acs.jpcc.1c07929
        """
        self.excited = False
        self.molecule = ase.Atoms(atom_list)
        # guesstimate reach in Angstroms
        # rmax for tetracene in
        # https://pubs.acs.org/doi/full/10.1021/acs.jpcc.1c07929
        self.reach = 80
        self.dipole = np.array([0, 1, 0])
        self.Lambda = 4.8e-20

    def __str__(self):
        "Stringify the Molecule, by printing the positions of both atoms."
        atoms = self.molecule.get_positions()
        return str(atoms)

    def excite(self):
        "Assign this molecule to be excited."
        self.excited = True

    def transition_probability():
        "Calculate the probability of transition."
        pass

    def get_position(self):
        """
        Get the position of this molecule.

        :return: The average position between all atoms in this molecule.
        """
        pos = self.molecule.get_positions()
        return np.average(pos, axis=0)

    def transition_charge():
        "Calculate the transition charge."
        pass


 
