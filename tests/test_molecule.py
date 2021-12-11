# test_molecule.py
import molecule as m
import mysite as site
import numpy as np
import ase

def test_pointparticle():
    atom_list = []
    atom_list.append(ase.Atom('N',(0,0,0)))
    atom_list.append(ase.Atom('N',np.array([1.08,0,0])))
    molec = m.Molecule(*atom_list)
    assert np.array_equal(molec.get_position(), np.array([0.54,0,0])) 
    assert isinstance(p, site.Site)
