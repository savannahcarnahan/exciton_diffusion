import numpy as np
from abc import abstractmethod
import site
import atom
import pointparticle

class coupling:
    
    epsilon = 8.854e-12 # Unit Fm-1
    
    # def __init__(self, dipole1, dipole2, R):
    #     self.dipole1 = dipole1
    #     self.dipole2 = dipole2
    #     self.R = R
    
    @abstractmethod
    def get_coupling():
        pass

#====================================================================    
# SUBCLASS1: dipole_dipole coupling model
class dip_dip_Hab(coupling):
    
    def get_coupling(self, site1, site2):
        # Assuming dipole1, dipole2 and R are numpy arrays
        # dipole1: transition dipole of a site1
        # R: distance vector between site1 and site2
        
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
        Hab = (1/(4*np.pi*self.epsilon))*k*(mag_u1*mag_u2)/(mag_R)**3
        
        return Hab

# SUBCLASS2: transition charge method    
class trans_charge(coupling):
    pass
