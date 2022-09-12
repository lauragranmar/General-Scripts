import os, sys, glob
from subprocess import call


currentdir = ". "
for root, dirs, files in os.walk(".", topdown=False,):
    for name in dirs:
        currentdir = (os.path.join ( root,name ))
        #print "this is a directory", (os.path.join(root, name))

    for f in files:
        #print "this is a file", (os.path.join(root, f))
        pathtofile = (os.path.join(root, f))
        abspath = " . "
        text = " . "

        if "fe.dat" in pathtofile:
            abspath = os.path.abspath(pathtofile)
            print "found fe.dat", pathtofile
            #print "this is the abs path", abspath
            with open ( pathtofile,'r' ) as fileobj:
                text = fileobj.readlines()[-1]
            print(text)

            with open ( "energysummary.txt","a" ) as outputfile:
                print >> outputfile,abspath,"\n"
                print >> outputfile,text
                print >> outputfile,"               "
                print >> outputfile,"               "
                print >> outputfile,"               "
                print >> outputfile,"               "

