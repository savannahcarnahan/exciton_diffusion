import prob_rule
import arrhenius
import marcus
import FRET
def create(prob_rule_type):
    if prob_rule_type.lower() == 'arrhenius':
        return arrhenius.Arrhenius()
    elif prob_rule_type.lower() == 'marcus':
        return marcus.Marcus()
    elif prob_rule_type.lower() == 'fret':
        return FRET.fret()
    else:
        raise ValueError(format)


