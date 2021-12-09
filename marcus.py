import prob_rule as p
import system
import pointparticle
import crystal
import math
import numpy as np
from scipy import constants
import Hab
class Marcus(p.ProbRule):
    
    # Global constants for marcus rate equation
    # hbar = 1.0545e-34
    # kb = 1.380e-23
    # T = 293
    
    # creates the correct probability rule
    def __init__(self):
        pass
    
    # def marcus_rate(self, Hab, Lambda):
    #     k_ab = (2*np.pi/self.hbar)*(np.sqrt(1/(4*np.pi*self.kb*self.T*Lambda))*(Hab**2)*np.exp(-(Lambda/4*self.kb*self.T)))
    #     return k_ab
    # Need H_ab (between site a and b)


    def transition_prob(self, site1, site2, system):
        R = np.subtract(site1.get_position(), site2.get_position())
        coul_coupling = Hab.dip_dip_Hab()
        Jcoul = coul_coupling.get_coupling(site1.dipole, site2.dipole, R)
        k_ab = (2*np.pi/constants.hbar)*(np.sqrt(1/(4*np.pi*constants.Boltzmann*293*site1.Lambda))*(Jcoul**2)*np.exp(-(site1.Lambda/4*constants.Boltzmann*293)))
        return k_ab
        
    # calculates the probability with the equation
    # k_ab = 2*pi/hbar(1/sqrt(4*pi*lambda*kb*T)*H_ab^2*e^(-1/kb*T))
    # lambda = 0.3 eV (usually for energy transfer)
    # tunneling is ignored
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6-7
    # def transition_prob(site1, site2, system):
    #     p.transition_prob(site1, site2)
    #     # place holder until implementation
    #     prob = 0.0001
    #     return prob
