import numpy as np
import crystal
import system
import mysite as site
import pointparticle as pt

def test_crystal():

    site1 = pt.PointParticle(np.array([1,0,0]))

    site2 = pt.PointParticle(np.array([0,1,0]))

    syst = crystal.Crystal('arrhenius', 'kmc', [site1, site2], 3)
    assert issubclass(crystal.Crystal, system.System)

    setattr(site1,'excited',True)
