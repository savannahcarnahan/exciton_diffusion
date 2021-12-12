from inputprocessor import process_input
from pointparticle import PointParticle
from molecule import Molecule
def test_inputprocessor(in_file = 'test_input.txt', in_file2 = 'test_input2.txt',
        in_file3 = 'test_molecule.txt'):
    system_type, site_list, dimen, rate, model_type, start_time, end_time = process_input(in_file)
    assert system_type == 'crystal'
    assert dimen == 3
    assert rate == 'marcus'
    assert model_type == 'kmc'
    assert start_time == 0
    assert end_time == 10
    assert isinstance(site_list[0], PointParticle)

    system_type, site_list, dimen, rate, model_type, start_time, end_time = process_input(in_file2)
    assert system_type == 'crystal'
    assert dimen == 3
    assert rate == 'arrhenius'
    assert model_type == 'kmc'
    assert start_time == 0
    assert end_time == 10
    assert isinstance(site_list[0], PointParticle)


    system_type, site_list, dimen, rate, model_type, start_time, end_time = process_input(in_file3)
    assert system_type == 'crystal'
    assert dimen == 3
    assert rate == 'marcus'
    assert model_type == 'kmc'
    assert start_time == 0
    assert end_time == 10
    assert isinstance(site_list[1], Molecule)
