#! /usr/bin/env python
import numpy as np
import os, sys
from functools import reduce
"""
This is an aproximated calcualtion of the d band center. Do not use. 

Here it is calculated as that is the sumatoin of density of states (y) * the energy ( x)  in the range of the band ( total density of staes.)
For an accurate calculation see d_band_momnets.ipynb 

"""


"""Variables, Number of states, sumatioxn of moments """

#open file
#Flags : file fermi energy
"""
directorypath = os.getcwd()
dbandenergyFile = os.path.abspath(sys.argv[1])
fermiEnergy = os.path.abspath(sys.argv[2])
"""

dbandenergyFile= "MgO_100_ads_IrPt_Otop_gauss.projwfc.dat.pdos_atm#50(Pt)_wfc#1(d)"
#dbandenergyFile= os.path.abspath(sys.argv[1])
#reading the file
data = np.genfromtxt(fname=dbandenergyFile, skip_header=1, usecols=(0,1), dtype= ['float', 'float'], names=['E', 'PDOS'] )
fermiEnergy = 0.3809



def map2 (list1, list2, function):

    list3 = []
    for i in range(0, len(list1)):
       list3.append(function(list1[i], list2[i]))

    return list3


def summation (list):
    return reduce(lambda element1, element2: element1 + element2, list, 0)

def calculateDband(Energy, PDOS):
    momentsacrosstheDband = map2(Energy, PDOS,lambda E, pdos: E * pdos) # returns a list after trasnforming it.
    mean = np.mean(momentsacrosstheDband)
    sumofmoments = summation(momentsacrosstheDband)
    #sumofmomentssquared = (sumofmoments)**2
    count = len(Energy)
    #print "Ed calculated as sumofmoments/count =", sumofmoments/count 

    return mean

print " Ed-refEf=", calculateDband(data['E']-fermiEnergy, data['PDOS'])

print " Ed =", calculateDband(data['E'], data['PDOS'])


