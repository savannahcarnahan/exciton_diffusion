import prob_rule as p
import system
import pointparticle
import crystal
import math
import numpy as np
from scipy import constants
# import hab
class Marcus(p.ProbRule):
    
    # Global constants for marcus rate equation
    # hbar = 1.0545e-34
    # kb = 1.380e-23
    # T = 293
    
    # creates the correct probability rule
    def __init__(self):
        pass

    def dip_dip_hab(self, site1, site2):
        # Assuming dipole1, dipole2 and R are numpy arrays
        # dipole1: transition dipole of a site1
        # R: distance vector between site1 and site2
        epsilon = 8.854e-12 # Unit Fm-1 
        dipole1 = getattr(site1, 'dipole')
        dipole2 = getattr(site2, 'dipole')
        R = site1.get_position() - site2.get_position()

        # converting all the vectors to unit vectors
        unit_u1 = dipole1/np.linalg.norm(dipole1)
        unit_u2 = dipole2/np.linalg.norm(dipole2)
        unit_R = R/np.linalg.norm(R)

        # k: Orientation factor
        k = np.dot(unit_u1, unit_u2) - 3*np.dot(unit_u1, unit_R)*np.dot(unit_u2, unit_R)

        # Converting debyee to coulombmeter (SI)
        mag_u1 = np.linalg.norm(dipole1)*3.3356e-30
        mag_u2 = np.linalg.norm(dipole2)*3.3356e-30
        mag_R = np.linalg.norm(R)*1e-10 # Converting angstrom to meters
        hab = (1/(4*np.pi*epsilon))*k*(mag_u1*mag_u2)/(mag_R)**3

        return hab 
    
    # def marcus_rate(self, Hab, Lambda):
    #     k_ab = (2*np.pi/self.hbar)*(np.sqrt(1/(4*np.pi*self.kb*self.T*Lambda))*(Hab**2)*np.exp(-(Lambda/4*self.kb*self.T)))
    #     return k_ab
    # Need H_ab (between site a and b)
    def transition_prob(self, site1, site2, system):
        pi = np.pi
        T = system.T
        kb = constants.Boltzmann
        Lambda = site1.Lambda
        hbar = constants.hbar
        Jcoul = self.dip_dip_hab(site1, site2)
        k_ab = 10**-12 * (2*pi/hbar)*(np.sqrt(1/(4*pi*kb*T*Lambda))*(Jcoul**2)*np.exp(-(Lambda/4*kb*T)))
        return k_ab
    
    
