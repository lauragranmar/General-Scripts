#/bin/bash

for dir in */
do

if [ -f '.DS_Store' ]
then

cd $dir
rm .DS_Store

fi
#cd /Users/lauragranda/Documents/DFT-Essentials-someProjects/General-Scripts
done