#!/bin/bash
#ALiases
baderclean=$HOME/apps/bader.sh
vclean=$HOME/apps/vtstscripts-929/vcleanlpg.sh

mkdir BADER
mkdir arxiv

$baderclean BADER

$vclean arxiv
cd arxiv 
#gunzip OUTCAR.gz
#cp OUTCAR ../
#gzip OUTCAR
cd ..


















