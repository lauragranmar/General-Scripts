#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                                                 
#begining of outer loop                                                                                                                                                                     
for dir in */ ; do
cd $dir
molecule=${PWD##*/}
E=`grep 'sigma' OUTCAR | tail -n1`

cat>> ../energies$name.txt <<EOF
${PWD##*/}  ${E}
EOF

cd ..
done



echo





exit 0

