import unittest
import numpy as np
import crystal
import system
import static
import mysite as site
import pointparticle as pt
from prob_rule import ProbRule
from model import Model
from marcus import Marcus
from arrhenius import Arrhenius
from kmc import KMC

site1 = pt.PointParticle(np.array([1,0,0]))

site2 = pt.PointParticle(np.array([0,1,0]))

setattr(site1,'excited',True)

site_list = [site1, site2]
    
rate = Arrhenius()

model = KMC()

class TestSystems(unittest.TestCase):
    def test_crystal(self):
        syst = crystal.Crystal(rate, model, site_list, 3)
        assert issubclass(crystal.Crystal, system.System)
        assert isinstance(getattr(syst, 'rate'), ProbRule)
        assert isinstance(syst.model, Model)
        assert isinstance(syst.site_list, list)
        assert syst.dimen == 3
        assert syst.T == 298

    def test_static(self):
        syst = static.Static(rate, model, site_list, 3, 0) 
        assert issubclass(static.Static, system.System)
        assert isinstance(syst.rate, ProbRule)
        assert isinstance(syst.model, Model)
        assert isinstance(syst.site_list, list)
        assert syst.dimen == 3
        assert syst.T == 0
