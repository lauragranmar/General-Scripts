#! /usr/bin/env python
import numpy as np
import os, sys
from ase import Atoms, Atom
from ase.constraints import *
from ase.io import read, write
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.vasp import *

'''' The default of direct = False is turn to True in the io/vasp.py line 629, module from this ase package.
USE: pythonscript < CONTCAR >  <xyz>  < number of atoms fix >
'''

# IT is also possible to implicitly parse the atomic positions and lattice parameters from CONTCAR
# The problem with this is that methods are not recognizable within the pycharm IDE.


def read_contacar(contcar):


    return read(contcar,format='vasp')
CONTCAR_x= read_contacar(contcar=os.path.abspath(sys.argv[1]))


def read_waterlayer(xyz):
    '''read xyz file and generate atoms object'''
    return read(xyz, format='xyz')
WL =  read_waterlayer(xyz=os.path.abspath(sys.argv[2]))


##Getiing the cell lattice vectors from contcar file

cell = CONTCAR_x.get_cell()

#setting the waterlayer positions accodinggly to the new cell
WL.set_cell(cell) # not scaled atoms as it is the same cell

# extending (appending) the  water layer on the previous cell
CONTCAR_x.extend(WL)

#Setting constraints for the optimization. The two bottom layers of the slab are fixed.
fixatoms_constraint = int(sys.argv[3])

CONTCAR_x.set_constraint( FixAtoms( indices=range(fixatoms_constraint) ) )


# Writting the INPUT files
xc = str(sys.argv[4])
calc = Vasp (xc=xc , gamma=False, kpts=(8, 8, 1),
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True,
             #laechg=True,
             ncore= 12,
             ibrion=2,
             potim=0.24,
             algo='FAST',
             ismear=2,
             sigma=0.2,
             nelmin=8,
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
