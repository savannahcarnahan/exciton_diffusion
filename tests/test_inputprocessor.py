from input.inputprocessor import process_input
from pointparticle import PointParticle
def test_inputprocessor(in_file = 'examples/test_input.txt'):
    system_type, site_list, dimen, rate, model_type, start_time, end_time = process_input(in_file)
    assert system_type == 'crystal'
    assert dimen == 3
    assert rate == 'marcus'
    assert model_type == 'kmc'
    assert start_time == 0
    assert end_time == 10
    assert isinstance(site_list[0], PointParticle)
