
import os, sys, glob
from subprocess import call, Popen
""" This script is intended to clean files after  normal vasp optimization, it uses a modification of the script from vtst hankelman goup."""

#VARIABLES
path_to_sendjob_cartesius = "."
path_sendjob_hexa = ". "

top = os.getcwd()
for root, dirs, files in os.walk(".", topdown=False,):
    for f in files:
        os.chdir(root)
        pathtofile = os.path.join (root,f )
        if "WAVECAR" in pathtofile:
            abspath = os.path.abspath (pathtofile )
            print "found WAVECAR",pathtofile
            os.chdir(os.getcwd())
            os.mkdir ( 'FREQS' )
            call ( ['cp','CONTCAR','FREQS/'] )
            call(["/home/granmar/apps/vclean3.sh"])


            print "this is the abs path", abspath



        os.chdir(top)
