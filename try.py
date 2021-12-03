import system_factory
import crystal
import numpy as np
import pointparticle as pt

site1 = pt.PointParticle(np.array([1,0,0]))

site2 = pt.PointParticle(np.array([0,1,0]))

syst = system_factory.create('crystal', [site1, site2], 3, 'Arrhenius')


print(site1)
print(site2)
neighbors = crystal.Crystal(syst.get_neighbors(site1),3, 'Arrhenius')
print(neighbors)


