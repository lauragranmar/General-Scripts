#! /usr/bin/env python
__author__ = 'lauragranda'

import numpy as np
import os, sys
from ase import Atoms, Atom
from ase.constraints import *
from ase.io import read, write
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.vasp import *

'''
Allows to create the input files by setting a different exchange correaltion functional (xc variable).
$ thisscript.py CONTCAR constraintAtoms xc-labe
See ASE documentation for more info.

The default of having the coordinates in cartesians in turned off by setting direct = True in the io/vasp.py line 629, module from this ase package.
In this way we get coordiantes in direct units ( or fractional units)
'''

# IT is also possible to implicitly parse the atomic positions and lattice parameters from CONTCAR
# The problem with this is that methods are not recognizable within the pycharm IDE.


def read_contacar(contcar):
    return read(contcar,format='vasp')

CONTCAR_x= read_contacar(contcar=os.path.abspath(sys.argv[1]))


#VARIBLES
##Getiing the cell lattice vectors from contcar file
cell = CONTCAR_x.get_cell()

#Setting constraints for the optimization. The two bottom layers of the slab are fixed.
fixatoms_constraint = int(sys.argv[2])
CONTCAR_x.set_constraint(FixAtoms(indices=range(fixatoms_constraint))) #


print 'cell from CONTCAR:\n', CONTCAR_x.get_cell ()
#print 'positions with wrap = False', CONTCAR_x.get_positions (wrap=False)
#print "positons with wrap + TRUE", CONTCAR_x.get_positions (wrap=True)

# Writting the INPUT files
xc= str(sys.argv[3])
calc = Vasp (xc= xc, gamma=False, kpts=(8, 8, 1),
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True,
             # laechg=True,
             ncore= 8,
             ibrion=1,
             potim=0.24,
             algo='NORMAL',
             ismear=2,
             sigma=0.2,
             nelmin=8,
             nsw=1500,
             ediff=1.0e-6,
             ediffg= -0.01) # change this accordingly.

calc.calculate (CONTCAR_x)
# calc.write_sort_file(CONTCAR_x)
# poscar=write('POSCAR2',CONTCAR_x, format='vasp', direct=True)

# calc.write_kpoints()
# calc.write_incar(calc)
calc.write_potcar ()

