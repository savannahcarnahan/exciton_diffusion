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
k = prob_rule_factory.create('fret')


def test_fret_rate():
    assert k.dip_dip_hab(p1, p2) < 10e-15 # Usually less than 
