import prob_rule as p
import system
class Arrhenius(p.ProbRule):
    
    # creates the correct probability rule
    def __init__(self):
        pass

    # calculates the probability with the equation
    # k_12 = v_eff * e^((-1/kb*T)*delta_G - correction_factor)
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6
    def transition_prob(self, site1, site2, system):
        #p.transition_prob(site1, site2)
        # place holder until implementation
        prob = 1
        return prob
