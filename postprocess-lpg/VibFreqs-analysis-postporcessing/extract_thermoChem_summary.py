import os, sys, glob
from subprocess import call

'''
Extracts thermochemical corrections data. The output file from this python script is not easy to parse a better output orgainized as a data frame can be obtained from getfreqs.sh script written in bash.
'''
currentdir = ". "
for root, dirs, files in os.walk(".", topdown=False,):
    for name in dirs:
        currentdir = (os.path.join ( root,name ))
        #print "this is a directory", (os.path.join(root, name))

    for f in files:
        #print "this is a file", (os.path.join(root, f))
        pathtofile = (os.path.join(root, f))

        if "Thermochemistry.txt" in pathtofile:
            abspath = os.path.abspath(pathtofile)
            print "found Thermochemistry.txt", pathtofile
            #print "this is the abs path", abspath
            with open ( pathtofile,'r' ) as fileobj:
                textfile = " . "
                for lines in fileobj:
                    textfile += lines

            #print(text)

            with open ( "ZPE_TS_Summary.txt","a" ) as outputfile:
                print >> outputfile,"==============="
                print >> outputfile, pathtofile
                print >> outputfile,abspath,"\n"
                print >> outputfile,textfile
                print >> outputfile,"               "
                print >> outputfile,"               "
                print >> outputfile,"               "
                print >> outputfile,"==============="
