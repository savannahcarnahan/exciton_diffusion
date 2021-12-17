"""
Point Particle
================
"""
import atom
import numpy as np


class PointParticle(atom.Atom):
    """
    The Point Partcicle class implements a particle representing an atom.
    """
    def __init__(self, *coord, Lambda = 4.8e-20, reach = 80):
        """
        Initialize a Point Partcicle.

        :param coord: A list of coordinates for the particle's initial position.
        """
        self.excited = False
        self.Lambda = Lambda
        self.dipole = np.array([0, 1, 0])
        self.position = np.asarray(coord)

        # should be replaced later maybe?
        # tells function how far away neighbors can be
        self.reach = reach

    def __str__(self):
        """
        Stringify the Point Particle's position, to print it as a list.
        """
        print(self.position)
        return str(self.position)
 
    def get_position(self):
        """
        Get the position of the particle.
        :return: the position of the particle.
        """
        return self.position
