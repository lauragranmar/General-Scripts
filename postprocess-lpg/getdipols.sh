#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                   
getforces='/home/laura/apps/vtstscripts-929home/vef.pl'

#begining of outer loop                                                                                                                                                                     
for dir in */ ; do
cd $dir

grep dipolmoment OUTCAR | tail -1 | awk '{print $4}'
#$getforces

molecule=${PWD##*/}

F=`grep dipolmoment OUTCAR | tail -1 | awk '{print $4}'`

cat>> ../dipols_$name.txt <<EOF
${PWD##*/}  ${F}
EOF

cd ..
done



echo

column  -t dipols_$name.txt >> dipols$name.txt
rm  dipols_$name.txt




exit 0

