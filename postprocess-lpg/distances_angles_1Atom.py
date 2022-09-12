#! /usr/bin/env python
__author__ = 'lauragranda'

import sys
import  os
import numpy as np
from numpy import linalg as LA
from decimal import Decimal


'''This script return desired distances between the the adsrobate and the 4 metals close to it in the unit cell
This particular one is hardcoded for the adsorbate H, but it can be reuse for the same # of atoms with adsorbate = O'''

directorypath = os.getcwd()
pwofile = os.path.abspath(sys.argv[1])

readlinesfile = [line.strip('\n') for line in open(pwofile, 'rb').readlines()]

#hard coded to extract the last four surface atoms plus water atoms.
last_lines= readlinesfile[-5:] # This takes the last lines and makes a list of

array= []
for i in last_lines:
    array.append(i[2:]) #

print "this is the first array", array
Data = np.genfromtxt(array, dtype='float')
print "This is the DATA array", Data

listData = list(enumerate(Data))


#Distance from plane to a point#

n= np.cross(Data[0], Data[1])

n_norm = LA.norm(n)


#points on the surface ( plane) using advanced idexing
P = Data[0]
Q = Data[1]
R = Data[2]

#point above the surface
W = Data[-1] # this means that the last element of the list ( the last coordinates) are taken as W.
print "THIS IS W (point above the surface", W

# get two vectors that are on the surface plane: PQ and PR

PQ = [Q[0] - P[0],Q[1]-P[1],Q[2]-P[2]]
PR = [R[0]-P[0],R[1]-P[1],R[2]-P[2]]

print "vector PQ", PQ

#Get the cross product of the vectors PQXPR to get its orthogonal vector( which is also the normal to the surface plane)
n = np.cross(PQ,PR)
n_norm = LA.norm(n)
N = n/n_norm

# To get the distance from the plane to a point W, I need a vector from the plane to point W that can be PW.
PW = [W[0] - P[0], W[1]-P[1], W[2]-P[2]]
print"PW\n:", PW


D= np.dot(N, PW)
#Then the distance between surface norml and point W is

print "distance from plane to point:", D


# uses direction vector surface normal ( n )
# Get the angle between Two vectors (One vector could be the bond of two atoms) and the other is the plane normal vector.
#If th Oxygen is K

J = Data[-1] #Last atom
K = Data[-2]# atom before the last atom

JK = [K[0]-J[0], K[1]-J[1], K[2]-J[2]]

JK_norm = LA.norm(JK)
dotproduct = np.dot(n, JK)
magnitudes = np.dot(JK_norm, n_norm)


cos_x = dotproduct/ magnitudes


print "H- AND SURF NORMAL cos_x", cos_x

arcos_x = np.degrees(np.arccos(cos_x))

print "ANGLE BETWEEN surface and H", arcos_x

from scipy.spatial import distance # calculates the distance betwen two point, given the coordinates.
Pd =  Data[-2] # atom before the last atom
H =   Data[-1] # last atom

#Metals
M1 =  Data[0]
M2 =  Data[1]
M3 =  Data[2]
M4 =  Data[3]


print "Metal 4 coordiantes:\n", M4, '\n'

if Pd.all() == M4.all():
    print "Pd data -2 is equal to M4 Data[3]"
else:
    print "not equal"



distPd_H = distance.euclidean(Pd, H) #
#distOH2 = distance.euclidean(H2, O)

dist_m1o = distance.euclidean(M1, H)
dist_m2o = distance.euclidean(M2, H)
dist_m3o = distance.euclidean(M3, H)
dist_m4o = distance.euclidean(M4, H)





#Advanced Indexing

#print "advanzedindexing", Data[[0],[0]]

####PRINTS###

print "first element of the list from the xyz file:", last_lines[0], "\n"
print "type of teh list:",type(last_lines), "\n"
print "lenght of the list:", len(last_lines), "\n"
print "originlArray;", last_lines, "\n"
print "newarray:", array, "\n"
print "listDATA", listData, "\n"
print 'newarray[0]', array[0], "\n"
print 'Data', Data, "\n"
print "datashape", Data.shape, "\n"


print "C-O", round(distPd_H, 2)
print "distance from plane to point:", D
print "angle C-O:", arcos_x


f = open('Dist_Angles_H.txt', 'a')
#print >> f, 'Filename:', distOH2  # or f.write('...\n')
#print >> f, "H-Pd1 dist       ", round(distPd_H, 2)
print >> f, "M1-H             ", round(dist_m1o,2)
print >> f, "M2-H             ", round(dist_m2o,2)
print >> f, "M3-H             ", round(dist_m3o,2)
print >> f, "M4-H             ", round(dist_m4o,2)
print >> f, "H_Pd-Surf ang    ", round(arcos_x,2)
print >> f, "Surface-H dist   ", round(D,2)

f.close()
