#! /usr/bin/env python
__author__ = 'lauragranda'

import sys
import  os
import numpy as np
from numpy import linalg as LA
from decimal import Decimal



directorypath = os.getcwd()
pwofile = os.path.abspath(sys.argv[1])

readlinesfile = [line.strip('\n') for line in open(pwofile, 'rb').readlines()]

#hard coded to extract the last four surface atoms plus water atoms.
last_lines= readlinesfile[-6:]

array= []
for i in last_lines:
    array.append(i[2:])

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
W = Data[-2]
print "THIS IS W (point above the surface", W

# get two vectors that are on the surface plane: PQ and PR

PQ = [Q[0] - P[0],Q[1]-P[1],Q[2]-P[2]]
PR = [R[0]-P[0],R[1]-P[1],R[2]-P[2]]

print "vector PQ", PQ

#Get the corss product of the vectors PQXPR to get its orthogonal vecotor( which is also the normal to the surface plane)
n = np.cross(PQ,PR)
n_norm = LA.norm(n)
N = n/n_norm

# To get the distance from the plane to a point W, I need a vector from the plane to point W that can be PW.
PW = [W[0] - P[0], W[1]-P[1], W[2]-P[2]]
print PW


D= np.dot(N, PW)
#Then the distance between surface norml and point W is

print "distance from plane to point:", D


# uses direction vector surface normal ( n )
# Get the angle between Two vectors (One vector could be the bond of two atoms) and the other is the plane normal vector.
#If th Oxygen is K

J = Data[-1] #Oxygen
K = Data[-2]# Carbon

JK = [K[0]-J[0], K[1]-J[1], K[2]-J[2]]

JK_norm = LA.norm(JK)
dotproduct = np.dot(n, JK)
magnitudes = np.dot(JK_norm, n_norm)


cos_x = dotproduct/ magnitudes


print "CO AND SURF NORMAL cos_x", cos_x

arcos_x = np.degrees(np.arccos(cos_x))

print "ANGLE BETWEEN surface and CO", arcos_x

from scipy.spatial import distance
C =  Data[-2] #A
O =  Data[-1] #B

#Metals
M1 =  Data[0]
M2 =  Data[1]
M3 =  Data[2]
M4 =  Data[3]



distCO = distance.euclidean(C,O)
#distOH2 = distance.euclidean(H2, O)

dist_m1o = distance.euclidean(M1,C)
dist_m2o = distance.euclidean(M2,C)
dist_m3o = distance.euclidean(M3,C)
dist_m4o = distance.euclidean(M4,C)





#Advanced Indexing

#print "advanzedindexing", Data[[0],[0]]

####PRINTS###
"""
print last_lines[0]
print type(last_lines)
print len(last_lines)
print "originlArray;", last_lines
print "newarray:", array
print "listDATA", listData
print 'newarray[0]', array[0]
print 'Data', Data
print "datashape", Data.shape
"""

print "C-O", round(distCO,2)
print "distance from plane to point:", D
print "angle C-O:", arcos_x


f = open('Dist_Angles.txt', 'a')
#print >> f, 'Filename:', distOH2  # or f.write('...\n')
print >> f, "C-O dist         ", round(distCO,2)
print >> f, "M1-C             ", round(dist_m1o,2)
print >> f, "M2-C             ", round(dist_m2o,2)
print >> f, "M3-C             ", round(dist_m3o,2)
print >> f, "M4-C             ", round(dist_m4o,2)
print >> f, "O-C-Surf ang     ", round(arcos_x,2)
print >> f, "Surface-C dist   ", round(D,2)

f.close()