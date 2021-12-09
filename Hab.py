import numpy as np
from abc import abstractmethod


class coupling:
    
    epsilon = 8.854e-12 # Unit Fm-1
    
    @abstractmethod
    def get_coupling():
        pass

#====================================================================    
# SUBCLASS1: dipole_dipole coupling model
class dip_dip_Hab(coupling):
    
    def get_coupling(self,dipole1, dipole2, R):
        # Assuming dipole1, dipole2 and R are numpy arrays
        # dipole1: transition dipole of a site1
        # R: distance vector between site1 and site2
        # k: Orientation factor
        k = np.dot(dipole1, dipole2) - 3*np.dot(dipole1, R)*np.dot(dipole2, R)
        
        Hab = (1/(4*np.pi*self.epsilon))*k*(np.linalg.norm(dipole1)*np.linalg.norm(dipole2))/(np.linalg.norm(R))**3
        
        return Hab

# SUBCLASS2: transition charge method    
class trans_charge(coupling):
    pass
