# preprocessing file to convert publised crystal format (.xyz) to dezired input

import sys
import re
import numpy as np


no_of_atoms = int(sys.argv[1]) # Number of atoms in the molecule
out_type = sys.argv[2] # output file name
file_name = sys.argv[3] # name of xyz file
out_name = sys.argv[4] # name of output

List = open(file_name).readlines() # Opening xyz file
#MOLECULE======================================================================
if out_type == 'molecule':
    list2 = []

    list2.append('molecule\n')
    for i, a in enumerate(List):
        list2.append(a), 
        if i % no_of_atoms == no_of_atoms - 1: 
            list2.append("molecule\n")
    list2.pop()  
    
    textfile = open(out_name, "w")
    for i in list2:
        textfile.write(i)
    textfile.close()
#POINTPARTICLE=================================================================
elif out_type == 'pointparticle':
    list2 = [] # List to insert coordinates

    for i, a in enumerate(List):
        list2.append(a)

    list3 = [] # Dumb list to format list2 
    for i in list2:
        i = i.strip()
        i = re.split(' +', i)
        # Remove empty strings from list
        i = list(filter(('').__ne__, i)) 
        del i[0]
        i[1] = i[1].strip()
        
        list3.append(i)
        
    list4 = np.array(list3)
    xyz = list4.astype(float)
    split_by = len(xyz)/no_of_atoms
    split = np.array_split(xyz, split_by)

    xyz_avg = [] # To get the final formated list
    for i in split:
        j = (np.add.reduce(i)/12)
        j = np.round(j, 2)
        j = j.astype(str)
        k = np.array(('pointparticle ')) # To add site_type
        j[0] = np.char.add(k, j[0])
        xyz_avg.append(j) # Adding site type to the coordinates
    np.savetxt(out_name, np.array(xyz_avg), fmt="%5s") 
#==============================================================================   
else:
    print('error in input')
 
