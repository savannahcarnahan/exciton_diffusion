"""
Site Factory
================

The factory function for generating sites.
"""
import atom
import molecule
import pointparticle as pt
import molecule
def create(site_type, *params):
    """
    Creates an object of a site class based on its format, and pass in the initialization parameters.

    :param site_type: The type of the site. Currently supported "atom", "pointparticle", and "molecule".
    """
    if site_type.lower() == 'atom':
        return atom.Atom(*params)
    elif site_type.lower() == 'pointparticle':
        return pt.PointParticle(*params)
    elif site_type.lower() == 'molecule':
        return molecule.Molecule(*params)
    else:
        raise ValueError(site_type)

