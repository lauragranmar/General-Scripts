#/bin/sh
jobPath=~/apps/boeddhajobscript16.sh
name=pw
#dir=ptb_15
#mkdir  $dir
#cd $dir

for i in 3.84 3.86 3.88 3.91 3.93 3.95 3.98 4.00 4.05 4.20 4.22 4.26
do
mkdir $i
cd $i

cp ../INCAR ./
cp ../KPOINTS ./
cp ../POTCAR ./
cat > POSCAR << !
'$name' fcc
$i
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
4
direct
0.0 0.0 0.0
0.0 0.5 0.5
0.5 0.0 0.5
0.5 0.5 0.0                   
!

sbatch -J $name $jobPath


cd ../



done

cd ../
