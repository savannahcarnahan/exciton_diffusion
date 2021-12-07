import prob_rule as p
import system
import math
class Marcus(p.ProbRule):
    
    # creates the correct probability rule
    def __init__(self):
        pass
    
    # Need H_ab (between site a and b)

    # calculates the probability with the equation
    # k_ab = 2*pi/hbar(1/sqrt(4*pi*lambda*kb*T)*H_ab^2*e^(-1/kb*T))
    # lambda = 0.3 eV (usually for energy transfer)
    # tunneling is ignored
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6-7
    def transition_prob(site1, site2, system):
        p.transition_prob(site1, site2)
        # place holder until implementation
        prob = 0.0001
        return prob
