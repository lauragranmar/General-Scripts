import os, sys, glob
from subprocess import call, Popen
""" """


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
            print os.getcwd()
            #call(["python","/Users/lauragranda/PycharmProjects/VaspInputs/vib_inputs_creator/vibrations_inputs_creator.py","CONTCAR"])
            call (["python","/home/granmar/apps/postprocess-lpg/vibrations_inputs_creator.py","CONTCAR", "FixAtomNumber"])
        os.chdir(top)
