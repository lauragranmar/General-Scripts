#!/bin/bash

set -x
set -e

VTSTPATH='/home/granmar/apps/vtstscripts-929'
bader='/home/granmar/apps/bader'
Dir="$1"

#copy files to bader dir

cp AECCAR? CHGCAR $Dir

#Go to Bader dir
cd $Dir

#Do sum AECCAR0 + AECCAR2

"$VTSTPATH/chgsum.pl" AECCAR0 AECCAR2

#Do bader with the created reference CHGCAR_sum

$bader CHGCAR -ref CHGCAR_sum


#delete files after use

rm -f CHGCAR AECCAR? CHGCAR_sum

#Return to working directory
cd ..


