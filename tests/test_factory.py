import unittest
import system_factory
import static
import crystal
import site_factory
import numpy as np
import pointparticle
import atom


class TestFactories(unittest.TestCase):
    def test_system_factory(self):
        c = system_factory.create('crystal', 'uniform', 'kmc', [], 3)
        assert isinstance(c, crystal.Crystal)
        s = system_factory.create('static', [], 3, rate = 'marcus', model = 'kmc')
    
    def test_site_factory(self):
        p = site_factory.create('pointparticle', 1, 0, 0)
        assert isinstance(p.get_position(), np.ndarray)
        assert isinstance(p, pointparticle.PointParticle)
        a = site_factory.create('atom', 'N', 1, 0, 0)
        assert isinstance(a.get_position(), np.ndarray)
        assert isinstance(a, atom.Atom)
