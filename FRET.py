import prob_rule as p
import system
import pointparticle
import crystal
import math
import numpy as np
from scipy import constants
class fret(p.ProbRule):
    
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
        k_fret = 10**-12 * (2*pi/hbar)*(Jcoul**2)*Qd*SPEC
        return k_fret