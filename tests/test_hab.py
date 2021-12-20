import pointparticle as pt
import mysite as site
import pointparticle as pt
import numpy as np
import prob_rule_factory
import prob_rule
import system

# Two particles 1 A apart
p1 = pt.PointParticle(1, 0, 0) 
p2 = pt.PointParticle(2, 0, 0)

# calling fret
f = prob_rule_factory.create('fret')
m = prob_rule_factory.create('marcus')
a = prob_rule_factory.create('arrhenius')
def test_hab():
    assert isinstance(f.dip_dip_hab(p1, p2), float)
    assert isinstance(m.dip_dip_hab(p1, p2), float)
    assert isinstance(a.dip_dip_hab(p1, p2), float)


