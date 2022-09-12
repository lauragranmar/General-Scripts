#! /usr/bin/env python
import numpy as np
import sys

''' USE: moments.py {file: PDOS_USER.dat} {limits for integration: int1 int2}

( DOS file contining #energy(x) and one additional column with the States of interest
this file is obtained from vaspkit 11, 115 selecting the atoms and the atomic orbitals. } see https://vaspkit.com/tutorials.html#extract-and-output-dos-and-pdos
The limits are for filtering the relevant data ie. after visualization.
Returns, the non central second moment ( this can be change in the script)
the first moment ( center of the band)
the second central moment is the band width.
A more vrsatile script for the caulculation of the first moment ( band center) and second moment ( width of the band) is postprocess-lpg/DOS/d_band_moments.ipynb
'''

File = sys.argv[1] # a file containing only the  bands interested if d( then the sum of all d)

first_limit_energy_i, second_limit_energy_j = float(sys.argv[2]), float(sys.argv[3])

#datas = np.loadtxt(File, dtype=np.float64, skiprows=1)

#data_tuple = datas[:,0], datas[:,1:]

datas = np.genfromtxt(File, dtype=float,skip_header=1, names=['Energy','states'])

x = datas['Energy']
y = datas['states']

datazip_tuple = (list(zip(x, y)))


filter_arr_tuple = []

for i in list(zip(x, y)):
    if i[0] >= first_limit_energy_i and i[0] <= second_limit_energy_j:
        filter_arr_tuple.append(True)
    else:
        filter_arr_tuple.append(False)


#print filter_arr_tuple

data = np.array(datazip_tuple)[filter_arr_tuple]

energies, states = data[:,0], data[:,1]


def get_distribution_moment(x, y, order=0):
    """Return the moment of nth order of distribution.

    1st and 2nd order moments of a band correspond to the band's
    center and width respectively.

    For integration, the trapezoid rule is used.
    From ASE DFT tools and GPAW codes. I modified original ASE, wich did not take the sqrt of the second moment.
    """

    x = np.asarray(x)
    y = np.asarray(y)

    if order == 0:
        return np.trapz(y, x)
    elif isinstance(order, int):
        return np.trapz(x ** order * y, x) / np.trapz(y, x)
    elif hasattr(order, '__iter__'):
        return [get_distribution_moment(x, y, n) for n in order]
    else:
        raise ValueError('Illegal order: %s' % order)

print 'non-central width:', get_distribution_moment(energies,states, order= 2)

pdos = states

energy = energies

I = np.trapz(pdos, energy)

center = np.trapz(pdos * energy, energy) / I
width = np.sqrt(np.trapz(pdos * (energy - center)**2, energy) / I)

print 'd-band center = %s eV\nd-band width = %s eV\nintegral=%s' % (center, width, I)