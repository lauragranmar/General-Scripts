#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                   
getforces='/home/laura/apps/vtstscripts-929home/vef.pl'

#begining of outer loop                                                                                                                                                                     
for dir in */ ; do
cd $dir

vef.pl
#$getforces

molecule=${PWD##*/}

F=`tail -n1 fe.dat`

cat>> ../forcess_$name.txt <<EOF
${PWD##*/}  ${F}
EOF

cd ..
done

column  -t forcess_$name.txt >> forcess$name.txt
rm forcess_$name.txt
echo





exit 0

