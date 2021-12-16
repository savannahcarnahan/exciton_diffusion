import prob_rule as p
import system
import pointparticle
import crystal
import math
import numpy as np
from scipy import constants
class FRET(p.ProbRule):
    
    # creates the correct probability rule
    def __init__(self):
        pass
    # Function to calculate spectral overlap
    def spec_overlap(self):
        return 1 # 
        
    # calculates the probability with the equation
    # k_12 = v_eff * e^((-1/kb*T)*delta_G - correction_factor)
    # Since we are dealing with same molecules, exponential goes to 0
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6
    def transition_prob(self, site1, site2, system):      
        pi = np.pi
        hbar = constants.hbar
        Qd = 1 # For most cases Qd = 1
        Jcoul = self.dip_dip_hab(site1, site2)
        SPEC = self.spec_overlap()
        scaling = 10e13
        k_fret = scaling*(2*pi/hbar)*(Jcoul**2)*Qd*SPEC
        return k_fret
