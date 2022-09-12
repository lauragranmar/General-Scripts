#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                   
getpartialchg='/home/laura/apps/add_partialCharges_xyz.py'
COLS=$(tput cols)
#begining of outer loop                                                                                                                                                                     
for dir in */ ; do
cd $dir
molecule=${PWD##*/}
cp arxiv/CONTCAR.xyz BADER/xyzfile
cd BADER

##Python script runs here### 
add_partialCharges_xyz.py xyzfile ACF.dat


#c=`tail -n13 *.xyz| sed -n -e 1,2p -e 5,6p |awk '{print $1"    "$5}'` #n= p =print
#-n-e takes the lines n, to n+1,p=p prints|the output of sed is sent to awk m the first coulum $1 and the fith $5 column are printed)
#awk '{total += $5}END{ print total} '` This , sums all the values in teh last column.

c=`tail -n4 *.xyz|awk '{print $1"    "$5}'` #n= p =print
totc=`tail -n4 *.xyz|awk '{total += $5}END{ print total} '`

h=`tail -n13 *.xyz| sed -n -e 1,9p |awk '{print $1"    "$5}'`
toth=`tail -n13 *.xyz| sed -n -e 1,9p |awk '{total += $5}END{ print total} '`
#q=`tail -n10 *.xyz| awk '{print"    "$1"   "$5}'`
#tot=`tail -n10 *.xyz| awk '{total += $5}END{ print total} '`




q=`tail -n1 *.xyz| awk '{print"    "$1"    "$5}'`

cat>> ../../chg_$name.txt <<EOF
$molecule ${q}
EOF

cd ..
cd ..
done

column -t chg_$name.txt >>partialchg$name.txt
rm chg_$name.txt

echo
