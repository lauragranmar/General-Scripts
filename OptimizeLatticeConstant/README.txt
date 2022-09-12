Script workflow
The scripts are run inside the main directory where the lattice constant directories are created.
MainDir/LC1, LC2 LC2 script1, script2, script3
Or they can be accessed from aliases.
------Workflow------
1. latticeScript.sh
2. getEnergies.sh
3. Lattice_constant.py

Explanation
1. Creates the directories with inputs for the calculation at a set lattice constant.
2. Extracts energy information.
3. Calculates lattice constant using ASE module.

Example directory
This directory contains inputs and outputs of two simulation runs at  2 different KPOINTS using pw91 exchange correlation functional.
