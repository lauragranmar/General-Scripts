import os, sys, glob
from subprocess import call, Popen
""" This script is intented to create i=frequency inputs inside the Freqs directory that already has the CONTCAR file
"""

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
            print "found FREQS"
            os.chdir(os.getcwd())
            call ( ["python","/home/granmar/apps/postprocess-lpg/vibrations_inputs_creator.py","CONTCAR"] )
            #call ( ["sbatch","/home/granmar/apps/surfsarasbatch.sh"] ) #uncomment this to send the calculationn.
            #call ( ["python","/Users/lauragranda/PycharmProjects/VaspInputs/vib_inputs_creator/vibrations_inputs_creator.py","CONTCAR"] )

            #os.chdir(root) # this is not necessary

        os.chdir(top)
