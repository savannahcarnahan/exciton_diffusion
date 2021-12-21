import unittest
import pointparticle as pt
import prob_rule_factory
# import prob_rule
import static
import kmc


p1 = pt.PointParticle(1, 0, 0)
p2 = pt.PointParticle(2, 0, 0)

model = kmc.KMC()

k = prob_rule_factory.create('fret')
m = prob_rule_factory.create('marcus')
a = prob_rule_factory.create('arrhenius')
u = prob_rule_factory.create('uniform')

syst = static.Static(k, model, [p1, p2], 3)

class TestProbRules(unittest.TestCase):
    # if the values are larger than this, system
    # will not be in the hopping regime 
    # and the site model breaks down
    def test_fret_rate(self):
        r = k.transition_prob(p1, p2, syst)
        assert check(r)
    
    def test_marcus(self):
        syst.rate = m
        r = m.transition_prob(p1, p2, syst)
        assert check(r)

    def test_arrhenius(self):
        syst.rate = a
        r = a.transition_prob(p1, p2, syst)
        assert check(r)

    def test_uniform(self):
        syst.rate = u
        r = u.transition_prob(p1, p2, syst)
        assert r == 1


def check(rate):
    if not (rate<10e18 and rate>=0):
        return False
    else:
        return True
