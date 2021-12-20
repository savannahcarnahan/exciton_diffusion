"""
FRET Method
===========
| The FRET method is a probability rule object for calculating the
| translation probability between two sites in a system.
"""
import prob_rule as p
import numpy as np
from scipy import constants


class FRET(p.ProbRule):
    """
    | The FRET class calculates the translation probability, implements the `ProbRule`
    | interface
    | Constants used in FRET rate equation:
    - :math:`\\overline{h}` = 1.0545e-34
    |
    """

    def __init__(self):
        """
        | Empty constructor
        |
        """
        pass
      
    # Function to calculate spectral overlap
    def spec_overlap(self):
        """
        | Calculates the spectral overlap. Currently always return 1.
        | :return: 1
        |
        """
        return 1 

    # calculates the probability with the equation
    # k_12 = 2*pi/hbar * (1/(4*pi*epsilon_0)^2) * Qd *
    #           spec_overlap * J_coul^2
    # see https://pubs.acs.org/doi/full/10.1021/acs.jpcc.1c07929
    def transition_prob(self, site1, site2, system, Qd = 1):
        """
        | Calculate the transition probability between two sites using the FRET method.
        | The probability is calcualted using the equation :math:`k_{12}=\\frac{2\\pi}{\\overline{h}}\\cdot \\frac{1}{(4\\pi \\epsilon_0)^2} \\cdot Q_d \\cdot SO \\cdot H_{ab}`, 
        | where :math:`SO` is the spectral overlap and :math:`H_{ab}` is the coupling between the two sites.
        |
        | See `Singlet Exciton Dynamics of Perylene Diimide- and Tetracene-Based Hetero/Homogeneous Substrates via an Ab Initio Kinetic Monte Carlo Model <https://pubs.acs.org/doi/full/10.1021/acs.jpcc.1c07929>`_
        |
        :param site1: The first site containing the dipole
        :param site2: The second site containing the dipole
        :param system: The system these particles are in
        :param Qd: :math:`Q_d`. For most cases, we have :math:`Q_d=1`.

        :return: :math:`k_{12}`
        """
        pi = np.pi
        hbar = constants.hbar
        # Qd = 1 # For most cases Qd = 1
        Jcoul = self.dip_dip_hab(site1, site2)
        SPEC = self.spec_overlap()
        scaling = 10e13
        k_fret = scaling*(2*pi/hbar)*(Jcoul**2)*Qd*SPEC
        return k_fret
