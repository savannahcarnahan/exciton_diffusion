import atom
import molecule
import pointparticle as pt

def create(site_type, *params):

    if site_type.lower() == 'atom':
        return atom.Atom(*params)
    elif site_type.lower() == 'pointparticle':
        return pt.PointParticle(*params)
    elif site_type.lower() == 'molecule':
        return molecule.Molecule(*params)
    else:
        raise ValueError(site_type)

