#/bin/bash

freqs='/home/granmar/apps/postprocess-lpg/vibrations_inputs_creator.py'


for dir in */ 
do
cd $dir

cd FREQS/

$freqs CONTCAR 24 # here 24 atoms are fixed.

cp ../KPOINTS ./

cd ../

cd ../



done

cd ../

