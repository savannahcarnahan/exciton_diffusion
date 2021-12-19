# test_site.py
import unittest
import pointparticle as pt
import mysite as site
import molecule as m
import atom
import ase
import numpy as np


class TestSites(unittest.TestCase):

    def test_pointparticle(self):
        p = pt.PointParticle(1, 0, 0)
        assert np.array_equal(p.get_position(), np.array([1,0,0])) 
        assert isinstance(p, site.Site)

    def test_atom(self):
        a = atom.Atom('O', 1, 0, 0)
        assert np.array_equal(a.get_position(), np.array([1,0,0]))

    def test_molecule(self):
        atom_list = []
        atom_list.append(ase.Atom('N',(0,0,0)))
        atom_list.append(ase.Atom('N',np.array([1.08,0,0])))
        molec = m.Molecule(*atom_list)
        assert np.array_equal(molec.get_position(), np.array([0.54,0,0])) 
        assert isinstance(molec, site.Site)

