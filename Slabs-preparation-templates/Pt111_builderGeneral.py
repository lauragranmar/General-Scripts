from ase import Atoms, Atom
import numpy as np
from ase.io import write, read
from ase.calculators.vasp import *
from ase.constraints import *
from ase.build import fcc111, root_surface


#Info for POSCAR
latticeconstant= 3.9766 # optimized LC for xc = pbe 
slab = fcc111('Pt', size=(1,1,4), a=latticeconstant, vacuum=10.6)
slab = root_surface(slab, 3)
slab.center(about=3.5)

#Setting constraints for the optimization. The two bottom layers of the slab are fixed r3xr3 = 3 atoms per layer.
slab.set_constraint( FixAtoms( indices=range( 6 ) ) )

##INPUT CREATOR PARAMETERS##
calc = Vasp (xc='PBE', gamma=False, kpts=(kpointx, kpointy, 1),  #change kpoint to the optimized parameter
             istart=0,
             iniwav=1,
             icharg=2,
             encut=450,
             ldipol=True,
             idipol=3,
             lcharg=True,
             laechg=True,
             ncore= 4,
             ibrion=2,
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


