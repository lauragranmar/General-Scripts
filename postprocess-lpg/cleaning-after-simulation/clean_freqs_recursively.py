import os, sys, glob
from subprocess import call, Popen
""" This script cleans the Freqs directory after a vibrational analysis """

#VARIABLES
path_to_sendjob_cartesius = "."
path_sendjob_hexa = ". "

top = os.getcwd()
for root, dirs, files in os.walk(".", topdown=False):
    for d in dirs:
        os.chdir(root)


        pathtodir= os.path.join(root, d)
        #print "this is a directory",(os.path.join ( root,f ))
        #print "pathdir", pathtodir
        if "FREQS" in pathtodir:
            print "found FREQS"
            freqsdir =  os.chdir(('FREQS'))
            for root,dirs,files in os.walk(".", topdown=False):
                for f in files: 
                    pathtofiles = os.path.join(root, f)
                    if "WAVECAR" in pathtofiles:
                        print"found WAVECAR, cleaning starts"
                        call(["/home/granmar/apps/vclean3_freqs.sh"])

        os.chdir(top)
