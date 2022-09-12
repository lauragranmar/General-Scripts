#!/bin/bash                                                                                                                                                                                 
##RUN THIS SCRIPT INSIDE THE DIRECOTRY WHERE THE DIRECTORIES CONTAINING THE OUTPUTS FILES WHERE CREATED.                                                                                    
name=${PWD##*/}
outer=1 #outer loop counter                                                                                                                                   
#getforces='/home/laura/apps/vtstscripts-929home/vef.pl'
COLS=$(tput cols)
#begining of outer loop                                                                                                                                                                     
for dir in */ ; do
cd $dir


molecule=${PWD##*/}

cd FREQS/


F=`grep ! Thermochemistry.txt`
I=`grep f/i Thermochemistry.txt`

#printf "%-20s| " "${PWD##*/}\t" "$F" >> ../forces$name.txt
cat>> ../../summaryfreqs.txt<<EOF
${molecule}  ${F}

EOF

cat>>../../summaryfreqs_i.txt <<EOF
${molecule} ${I}
EOF
cd ..

cd ..

done

column  -t summaryfreqs.txt >> summaryfreqs_$name.txt
rm  summaryfreqs.txt
column  -t summaryfreqs_i.txt >> isummaryfreqs_$name.txt
rm summaryfreqs_i.txt
#echo

exit 0
