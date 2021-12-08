# test_pointparticle.py
import pointparticle as pt
import mysite as site
import numpy as np

def test_pointparticle():
    p = pt.PointParticle(1, 0, 0)
    assert np.array_equal(getattr(p, 'position'), np.array([1,0,0])) 
    assert isinstance(p, site.Site)
