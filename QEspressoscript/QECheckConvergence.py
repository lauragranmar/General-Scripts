#! /usr/bin/env python
import re, os, sys
import matplotlib.pyplot as plt
import numpy as np

"""This script plots the geometric step as a function of Energy,to veryfy the convergence trajectory. I made this particular script for outputs of the Quantum Espresso atomisitc simualtion program ca~2013"""

""" How to use the script: python name_of_scrip.py  pw-output File"""
directorypath = os.getcwd()
pwofile = os.path.abspath(sys.argv[1])

readlinesfile = [line.strip('\n') for line in open(pwofile, 'rb').readlines()]

grepEnergies = filter(lambda line: re.search('(!)', line), readlinesfile)

Data = np.genfromtxt(grepEnergies, dtype='float', usecols=4)

listData = list(enumerate(Data))

"""Make the convergence trip plot"""
x = map(lambda x: x[0] + 1, listData ) # extracts the first element of the tuple in the list which corresponds to the index ( GEOM Step)
y = map(lambda x: x[1], listData) # extracts the second element of the tuple in the list which corresponds to the energies

plt.plot(x,y, color= 'm', linewidth= 3, alpha = 0.4)
plt.show()