"""
Arrhenius method
================

The arrhenius method for calculating the translation probability between two sites.
"""
import prob_rule as p
import numpy as np
from scipy import constants


class Arrhenius(p.ProbRule):
    """
    The Arrhenius class calculates the translation probability, implements the `ProbRule` interface.

    Constants used in arrhenius rate equation:

    - :math:`k_B` = 1.380e-23
    - :math:`T` = 293
    """

    def __init__(self):
        "Empty constructor"
        pass

    # calculates the probability with the equation
    # k_12 = v_eff * e^((-1/kb*T)*delta_G - correction_factor)
    # see https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086 p. 6
    def transition_prob(self, site1, site2, system):
        """
        Calculate the transition probability between two sites using the arrhenius method.

        The probability is calcualted using the equation :math:`k_{12}=v_{\\text{eff}}e^{-\\frac{1}{k_B T}\\delta_G^0 - \\text{corrf}}`, 
        where :math:`corrf` is a correctoin factor. 

        Since the molecules are the same, we have :math:`\\delta_G^0=0`.

        See page 6 of `Charge Transport in Molecular Materials: An Assessment of Computational Methods <https://pubs.acs.org/doi/pdf/10.1021/acs.chemrev.7b00086>`_

        :param site1: The first site containing the dipole
        :param site2: The second site containing the dipole
        :param system: The system these particles are in

        :return: :math:`k_{12}`
        """
        T = system.T
        assert isinstance(T, float) or isinstance(T, int)
        kb = constants.Boltzmann
        assert isinstance(kb, float)
        DG = 0 # since molecules are same
        Jcoul = self.dip_dip_hab(site1, site2)
        assert isinstance(Jcoul, float)
        scaling = 10e23
        assert isinstance(scaling, float)
        k_ab = scaling*abs(Jcoul)*np.exp(-(1/kb*T)*DG)
        return k_ab
