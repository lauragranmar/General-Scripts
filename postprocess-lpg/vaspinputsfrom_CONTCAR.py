#! /usr/bin/env python
import numpy as np
import os, sys
from ase import Atoms, Atom
from ase.constraints import *
from ase.io import read, write
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.vasp import *


'''
Creates INCAR POTCAR and KPOINT, POSCAR files from the CONTCAR.

The default of having teh coordinates in cartesians in turned off by setting direct = True in the io/vasp.py line 629, module from this ase package.
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

#poscar = write ('POSCAR2', CONTCAR_x, format='vasp', direct=True, sort=False)

print 'cell from CONTCAR:\n', CONTCAR_x.get_cell ()
#print 'positions with wrap = False', CONTCAR_x.get_positions (wrap=False)
#print "positons with wrap + TRUE", CONTCAR_x.get_positions (wrap=True)

# Writting the INPUT files

calc = Vasp (xc='PBE', gamma=False, kpts=(4, 4, 1),
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True,
             lwave=False,
             #laechg=True,
             ncore= 12,
             ibrion=2,
             potim=0.34,
             algo='FAST',
             ismear=2,
             sigma=0.2,
             nelmin=8,
             nelm=80,
             nsw=1500,
             ediff=1.0e-6,
             ediffg= -0.02,
             isym = 0)

calc.calculate (CONTCAR_x)
# calc.write_sort_file(CONTCAR_x)
# poscar=write('POSCAR2',CONTCAR_x, format='vasp', direct=True)

# calc.write_kpoints()
# calc.write_incar(calc)
calc.write_potcar ()

