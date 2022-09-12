#/bin/sh
#jobPath=~/apps/boeddhajobscript16.sh #path to job script uncomment when necessary.
name=NiAl #chang name accordingly
#dir=ptb_15
#mkdir  $dir
#cd $dir
#MODIFY array with your sample of lattice constants
for i in 3.84 3.86 3.88 3.91 3.93 3.95 3.98 4.00 4.05 4.20 4.22 4.26
do
mkdir $i
cd $i
#these are the input files to start the calculation which are already made #uncoment if necesary
#cp ../INCAR ./
#cp ../KPOINTS ./
#cp ../POTCAR ./
cat > POSCAR << !
'$name'
$i
1.000000 0.000000 0.000000
0.000000 1.000000 0.000000
0.000000 0.000000 1.000000
Al Ni
1 1
direct
0.500000 0.500000 0.500000 
0.000000 0.000000 0.000000                
!

#sbatch -J $name $jobPath #this comand sends the calculation to the que is off /Turn ON if needed.


cd ../



done

cd ../
