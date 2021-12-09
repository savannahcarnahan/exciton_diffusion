import Hab
import marcus
import inputprocessor
import system_factory
import numpy as np

in_file = 'pytest_input.txt'

Jcoul = Hab.dip_dip_Hab()


system_type, site_list, dimen, rate, model_type, start_time, end_time = inputprocessor.process_input(in_file)
my_sys = system_factory.create(system_type, site_list, dimen, rate)

def test_customparam():
    dipole1 = np.array([0, 1, 0])
    dipole2 = np.array([0, 1, 0])
    R = np.array([0, 0, 1])
    assert Jcoul.get_coupling(dipole1, dipole2, R) < 1.98e-19 # Usually should be less than this value (10000 cm-1)
    assert rate.marcus_rate(Jcoul.get_coupling(dipole1, dipole2, R),  4.8e-20) < 1e+18  # Usually should be less than this value

# Testing between sites
for i in site_list:
    for j in site_list:
        if i != j:
            R = np.subtract(i.get_position(), j.get_position()) # Getting distance vector between sites
            rate = marcus.Marcus()
            def test_rate_for_site():
                assert Jcoul.get_coupling(i.dipole, j.dipole, R) < 1.98e-19 # Usually should be less than this value (10000 cm-1)
                assert rate.marcus_rate(Jcoul.get_coupling(i.dipole, j.dipole, R),  i.Lambda) < 1e+18 # Usually should be less than this value


