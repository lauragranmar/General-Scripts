#! /usr/bin/env python
__author__ = 'lauragranda'
#determining the lattice constant using equation of state Murnagham from ASE

import sys
from ase import Atom, Atoms
import numpy as np
from ase.eos import EquationOfState

file = sys.argv[1]

#file = 'energieskpts20.txt'

energyfile = np.genfromtxt(file, dtype=float, usecols=(0, 7), names = ['LC','en'])

a = energyfile['LC']
volumes = map(lambda i: (i**3)/4, a)
energies = energyfile['en']

eos = EquationOfState(volumes, energies, eos='murnaghan')
v0, e0, B = eos.fit()
a0_murnaghan = ((v0*4)**(1./3.))


#eos.plot('murnagham.png')


print " a0", round(a0_murnaghan,4)

f = open('eosparammeters.txt','w')

print>> f,"Lattice parameter fit to the equation of state using murnaghan eos"
print>> f,""
print>> f,"Minimum volume                    ", v0
print>> f,"Minimum Energy                    ", e0
print>> f,"Lattice Constant      (murnaghan):", a0_murnaghan
f.close()
