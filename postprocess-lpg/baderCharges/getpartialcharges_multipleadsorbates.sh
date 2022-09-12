#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                   
getpartialchg='/home/granmar/apps/add_partialCharges_xyz.py'
COLS=$(tput cols)
#begining of outer loop                                                                                                                                                                     
#for dir in */ ; do


molecule=${PWD##*/}
cp arxiv/CONTCAR.xyz BADER/xyzfile
cd BADER

##Python script runs here### 
add_partialCharges_xyz.py xyzfile ACF.dat


c=`tail -n10 *.xyz| sed -n -e 1,2p -e 5,6p |awk '{print $1"    "$5}'`
totc=`tail -n10 *.xyz| sed -n -e 1,2p -e 5,6p |awk '{total += $5}END{ print total} '`
h2o=`tail -n10 *.xyz| sed -n -e 3,4p -e 7,10p |awk '{print $1"    "$5}'`
toth2o=`tail -n10 *.xyz| sed -n -e 3,4p -e 7,10p |awk '{total += $5}END{ print total} '`
#q=`tail -n10 *.xyz| awk '{print"    "$1"   "$5}'`
#tot=`tail -n10 *.xyz| awk '{total += $5}END{ print total} '`

cat>> ../chg_$name.txt <<EOF
$molecule
COOH
${c}
totc ${totc}
------------
h2o 
${h2o}
toth2o ${toth2o}
EOF


cd ..
#done

column -t chg_$name.txt >>partialchg$name.txt
rm chg_$name.txt

echo

