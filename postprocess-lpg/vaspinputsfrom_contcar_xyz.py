#! /usr/bin/env python
import numpy as np
import os, sys
from ase import Atoms, Atom
from ase.constraints import *
from ase.io import read, write, iread
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.vasp import *


'''
 Creates INCAR POTCAR KPOINT and POSCAR files from an xyz file. 
The xyz system need to share the same cell parameters.
'''

"""
USE a previous contcar file to get the cell to pass it as an argument, then pass as an argument the xyz file with
the new coordiantes, and then  pass the selectie dynamics argument
.py <first argument ( CONTCAR) > <second argument (xyzfile )> <third argument (number of fixed atoms))>
"""

def read_contacar(contcar):
    ''' reads CONTCAR fil and gnerates atoms object'''

    return read(contcar,format='vasp')
CONTCAR_1= read_contacar( contcar=os.path.abspath( sys.argv[1] ) )

def read_xyz(xyz):
    ''''read xyz file and generate atoms object'''
    return read(xyz, format='xyz')

slab_x= read_xyz(xyz=os.path.abspath(sys.argv[2]))

cell = CONTCAR_1.get_cell()

#setting the waterlayer positions acordinggly to the new cell

slab_x.set_cell(cell) # not scaled atoms as it is the same cell
print slab_x

print "scaled positions", slab_x.get_scaled_positions(wrap=True)

#Setting constraints for the optimization. The two bottom layers of the slab are fixed.
fixatoms_constraint = int(sys.argv[3])
slab_x.set_constraint( FixAtoms( indices=range(fixatoms_constraint) ) ) 


print 'cell from CONTCAR:\n', slab_x.get_cell ()
print 'positions with wrap = False', slab_x.get_positions ( wrap=False )
print "positons with wrap + TRUE", slab_x.get_positions ( wrap=True )

# Writting the INPUT files
# change xc if needed.
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
             potim=0.24,
             algo='FAST',
             ismear=2,
             sigma=0.2,
             nelmin=8,
             nelm=80,
             nsw=1500,
             ediff=1.0e-6,
             ediffg= -0.02,
             isym = 0)

calc.calculate ( slab_x )
# calc.write_sort_file(CONTCAR_x)
# poscar=write('POSCAR2',CONTCAR_x, format='vasp', direct=True)

# calc.write_kpoints()
# calc.write_incar(calc)
calc.write_potcar ()

