import os, sys, glob
from subprocess import call, Popen
""" This script runs the Thermodynamicpp inside the FREQS directory"""

#VARIABLES
path_to_sendjob_cartesius = "."
path_sendjob_hexa = ". "

top = os.getcwd()
for root, dirs, files in os.walk(".", topdown=False,):
    for d in dirs:
        os.chdir(root)


        pathtodir= os.path.join(root, d)
        #print "this is a directory",(os.path.join ( root,f ))
        #print "pathdir", pathtodir
        if "FREQS" in pathtodir:
            print "found FREQS", pathtodir
            os.chdir('FREQS')
            #call(["gunzip", "OUTCAR.gz"])
            call(["python", "/home/granmar/apps/postprocess-lpg/Thermodynamicpp.py", "OUTCAR", "298.15"])
            #os.chdir(root) # this is not necessary

        os.chdir(top)


