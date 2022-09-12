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
last_lines= readlinesfile[-7:]

array= []
for i in last_lines:
    array.append(i[2:])


Data = np.genfromtxt(array, dtype='float')

listData = list(enumerate(Data))


#Distance from plane to a point#

n= np.cross(Data[0], Data[1])

n_norm = LA.norm(n)


#points on the surface ( plane) using advanced idexing
P = Data[0]
Q = Data[1]
R = Data[2]

#point above the surface
W = Data[-3]

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

J = Data[-2] #Hydrogen1
K = Data[-3]# Oxygen

JK = [K[0]-J[0], K[1]-J[1], K[2]-J[2]]

JK_norm = LA.norm(JK)
dotproduct = np.dot(n, JK)
magnitudes = np.dot(JK_norm, n_norm)


cos_x = dotproduct/ magnitudes


print "cos_x", cos_x

arcos_x = np.degrees(np.arccos(cos_x))

print "surface and H1-O", arcos_x

from scipy.spatial import distance
H1 =  Data[-2] #A
O  =  Data[-3] #B
H2 =  Data[-1] #C
#Metals
M1 =  Data[0]
M2 =  Data[1]
M3 =  Data[2]
M4 =  Data[3]



distOH1 = distance.euclidean(H1,O)
distOH2 = distance.euclidean(H2, O)

dist_m1o = distance.euclidean(M1,O)
dist_m2o = distance.euclidean(M2,O)
dist_m3o = distance.euclidean(M3,O)
dist_m4o = distance.euclidean(M4,O)



###Angle of the water
# Vector AB dot BC
#v_1 =  [O[0]-H1[0], O[1]-H1[1], O[2]-H1[2]]
v_1 = [H1[0]-O[0], H1[1]-O[1], H1[2]-O[2]]
v_2 = [H2[0]-O[0], H2[1]-O[1], H2[2]-O[2]]

magnitude_v1 = LA.norm(v_1)
magnitude_v2 = LA.norm(v_2)
dotproductofv1andv2_water = np.dot(v_1, v_2)
dotproductofMagnitudes_water = np.dot(magnitude_v1, magnitude_v2)

theta_water = dotproductofv1andv2_water/dotproductofMagnitudes_water
waterangle = np.degrees(np.arccos(theta_water))
print "WATER Angle", waterangle





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

print "H-O", round(distOH1,2),  distOH2
print "distance from plane to point:", D
print "angle H1-O:", arcos_x
print "H-O-H", waterangle

f = open('waterDist_Angles.txt', 'a')
#print >> f, 'Filename:', distOH2  # or f.write('...\n')
print >> f, "H-O dist         ", round(distOH1,2),"/", round(distOH2,2)
print >> f, "H-O-H ang        ", round(waterangle,2)
print >> f, "Surface-O dist   ", round(D,2)
print >> f, "H1-O-Surf ang    ", round(arcos_x,2)
print >> f, "M1-O             ", round(dist_m1o,2)
print >> f, "M2-O             ", round(dist_m2o,2)
print >> f, "M3-O             ", round(dist_m3o,2)
print >> f, "M4-O             ", round(dist_m4o,2)

f.close()
