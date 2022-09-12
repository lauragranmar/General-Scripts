#! /usr/bin/env python
import numpy as np
from ase.constraints import *
from ase import Atoms, Atom
from ase.io import read, write
from ase.constraints import *
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.vasp import Vasp
import sys, os
from ase.constraints import *

'''This script is intended for creating the INCAR POTCAR and KPOINT files for a harmonic vibrational analysis.
For this analysis a pre optimized structure is needed, therefore the CONTCAR file of the relaxed structure is pass in to this script.
use: python pythonscript.py CONTCAR natomsFixed'''


def read_contacar(contcar):
    return read(contcar,format='vasp')
atoms_in_contcar= read_contacar(contcar=os.path.abspath(sys.argv[1]))

#Set the numbre of atoms to fix for the vibrational anaysis
fixatoms_constraint = int(sys.argv[2])
atoms_in_contcar.set_constraint(FixAtoms(indices=range(fixatoms_constraint) ) ) #CHANGE THE Selective Dynamics for Vib analysis.


#Writting the INPUT files
#Parameters for the INCAR

calc = Vasp( xc='PBE', gamma= False, kpts=(8 , 8, 1), # Change the Kpts accordingly
             istart = 0,
             iniwav = 1,
             icharg = 2,
             encut = 450,
             ldipol = True,
             idipol = 3,
             prec = 'Accurate',
             lreal = False,
             lcharg = False,
             ibrion = 5,
             potim = 0.02,
             algo = 'V',
             ismear =0.,
             sigma = 0.1,
             nelmin = 4,
             nsw = 100,
             nfree = 2,
             ediff = 1.0e-6,
             isym = -1,
             npar = 4,
             isif = 0.)

calc.calculate(atoms_in_contcar)
calc.write_potcar() # normally this would work by itself by using calc.calculate.
