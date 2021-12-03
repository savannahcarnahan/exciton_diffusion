import prob_rule
import arrhenius
import marcus
def create(prob_rule_type):
    if prob_rule_type.lower() == 'arrhenius':
        return arrhenius.Arrhenius()
    elif prob_rule_type.lower == 'marcus':
        return marcus.Marcus()
    else:
        raise ValueError(format)


