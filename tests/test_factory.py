import system_factory
import crystal
import site_factory
import numpy as np
import pointparticle

def test_system_factory():
    c = system_factory.create('crystal',[], 3, 'marcus')
    assert isinstance(c, crystal.Crystal)
    p = site_factory.create('pointparticle', 1, 0, 0)
    assert isinstance(p.get_position(), np.ndarray)
    assert isinstance(p, pointparticle.PointParticle)
