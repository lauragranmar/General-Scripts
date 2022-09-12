from ase import Atoms, Atom
import numpy as np
from ase.io import write, read
from ase.calculators.vasp import *
from ase.constraints import *
from ase.build import fcc111, fcc100, fcc110, fcc211


#Info for POSCAR
latticeconstant= 3.9766 # optimized LC for xc = pbe 
slab = fcc111('Pt', size=(3,3,5), a=latticeconstant, vacuum=7.6) # 7.6 = 15.26 Vac
slab.center(about=4.8)

#Setting constraints for the optimization. The two bottom layers of the slab are fixed.
slab.set_constraint( FixAtoms( indices=range( 18 ) ) )
#Info for kpoints
lenghts= slab.get_cell_lengths_and_angles()






##INPUT CREATOR PARAMETERS##
calc = Vasp (xc='PBE', gamma=False, kpts=(kpointx, kpointy, 1), #change kpoint to the optimized parameter
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True,
             #laechg=True,
             ncore= 16,
             ibrion=1,
             potim=0.2,
             algo='NORMAL',
             ismear=2,
             sigma=0.2,
             nelmin=8,
             nsw=1500,
             ediff=1.0e-6,
             ediffg= -0.01)
calc.calculate(slab)
calc.write_potcar()


#Printing parameters
print '----------------','\n', 'cell'
print slab.get_cell()
print'-----------------', '\n','cell direct coordinates'
print slab.get_scaled_positions()
print '----------------', '\n', 'cell lattice vectors and angles'




