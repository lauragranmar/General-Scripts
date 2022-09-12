# My general Python and Shell scripts for Density Functional Theory calculations in the area of atomic scale materials modeling

This repository contains scripts for pre-processing and post-processing of data for Density Functional Theory calculations using [VASP](https://www.vasp.at), with [ASE](https://databases.fysik.dtu.dk/ase/ase/ase.html), and [VTST](https://theory.cm.utexas.edu/vtsttools/).

## Disclaimer

I do not intend to give a detailed explanation of how to run Density Functional Theory (DFT) calculations with VASP but rather to show an outline of the workflow I created using some of the scripts in this repo.

If you are a self-starter in computational chemistry and will be using DFT as a tool to learn about the amazing world between chemistry and material science! you might find some scripts useful.🤩

The majority of the scripts were made to solve problems at hand (hard-coded), but some scripts were made reusable to create useful workflows.

I also glued code from scripts I found on GitHub or from other open source codes. Appropriate authorship is kept inside the code.

I used the atomistic simulation environment (ASE) library and VTST tools, to create the majority of the scripts. Unfortunately, I found out about [vaspkit](https://vaspkit.com) at the end of my Ph.D., but I highly recommend it, it may save you a lot of time. From vaspkit I gathered and post-processed the density of states (DOS) of some systems.

For additional details see the  [ASE](https://databases.fysik.dtu.dk/ase/ase/ase.html), [VTST](https://theory.cm.utexas.edu/vtsttools/), or [VASP](https://www.vasp.at) documentation.

## Code requirements

* Python 2.7
* ASE 3.15
* VTST tools (vtst-929)

## Data analysis workflow

### 1/5 Start with a hypothesis

* This step helps design the system of the calculations. What is it that you are looking for? What property are you interested in studying? What is the influence of A on B? Why is Z behaving like that?

### 2/5 Prepare the system you want to model

* Prepare a plan of the various calculations you will need to run to obtain the data to answer your questions. Prepare the input files. These are the files that contain the information about the system you will model. For example, the xyz coordinates of the atoms. In VASP this is the POSCAR file.

### 3/5 Run the simulations and extract the data from the simulations

* The first may take time due to failed convergence, wrong input files, or just a big model with many atoms. But, once your system is finished reaching its most energetically favorable state, then proceed to post-processing. Again by knowing what you are looking for you can move toward the next question. For example, for the thermochemical energy corrections of an adsorbed molecule, we correct the energy with ZPE and S, which are obtained from a frequency calculation. For that, the output of the relaxed system is used as input for the next calculation.

### 4/5 Visualize the data

* Plot different variables, find trends, and re-plot. I mostly used Excell, Jupyter Notebook, and matplotlib. The python scripts used for plotting will be on separate repositories as per the project.

### 5/5 Report the findings, write your story and be happy

😊

## Job (calculation) workflow

### 1/5 Create Input Files and run some tests

To create input files, my preferred ways were sketching in the ASE GUI to generate the POSCAR, or coding using the ase.build method to build the POSCAR and all the inputs to run a VASP calculation. See  [Slabs-preparation-templates/](Slabs-preparation-templates/)

At this point, you also want to determine the initial parameters of the calculations, optimize lattice constants, and other parameters that will allow your calculation to be reproducible. See [OptimizeLatticeConstant/Lattice_constant.py](OptimizeLatticeConstant/Lattice_constant.py)

### 2/5 Run the simulations (jobs)

Set up your environment in the supercomputer ( ask for help ) and run your simulations. After the relaxation is finished (checked if the system has converged, by checking the forces on the atoms. See [postprocess-lpg/getforces.sh](postprocess-lpg/getforces.sh), this uses vef.pl from vtst.

### 3/5 Run the vibrational frequency analysis ( if you need )

I used IBRION = 5 parameter inside the INCAR file. Run a script to generate the INCAR, POTCAR, KPOINT, and new POSCAR files with the fixed atoms. See [postprocess-lpg/VibFreqs-analysis-postporcessing/vibrations_inputs_creator.py](postprocess-lpg/VibFreqs-analysis-postporcessing/vibrations_inputs_creator.py).

### 4/5 Extract the energies from the relaxed system and frequencies from the vibrational analysis

Extract all the data you want. Create more scripts if you need them. Note that the postprocessing analysis will be different depending on your system, for example, whether it is a gas-phase molecule or and adsorbed molecule. For scripts, see [postprocess-lpg/getEnergies.sh](postprocess-lpg/getEnergies.sh), and [postprocess-lpg/VibFreqs-analysis-postporcessing/](postprocess-lpg/VibFreqs-analysis-postporcessing/)

### 5/5 Run additional simulations to extract additional data

Analyze and ask if you need more information such as the density of states or partial charges. Depending on the data you need, you may run additional calculations with specific parameters, for example for the DOS analysis set LORBIT = 10 or 11.
See [postprocess-lpg/DOS/d_band_moments.ipynb](postprocess-lpg/DOS/d_band_moments.ipynb), and [postprocess-lpg/baderCharges](postprocess-lpg/baderCharges)
