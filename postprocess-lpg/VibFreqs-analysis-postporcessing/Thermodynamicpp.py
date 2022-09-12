#! /usr/bin/env python
__author__ = 'lauragranda'
import  sys, os
import numpy as np

"""
Thermochemical corrections based on the harmonic oscillator.
Calculates, ZPE, Svib at a given temperature.
Uses the OUTCAR file to get the data about the virational analysis.
This OUTCAR file is created after vib analysis in VASP, generally using IBRION = 5.
For more info, see VASP documentation on how to run a vibrational analysis.
"""


# IMPORTANT Physical Consntants from thermop ( https://github.com/guillemborrell/thermopy/blob/master/thermopy/constants.py)y##
# Consntnatname = (number, unit, uncertainty)
planck_constant_over_2_pi_in_ev_s = (6.58211915e-16, 'eV s', 5.6e-23)
speed_of_light_in_vacuum = (299792458., 'm s^-1')
boltzmann_constant_J_per_K= (1.3806505e-23, 'J K^-1', 2.4e-29)
boltzmann_constant_eV_per_K =( 8.6173303e-5, 'eV K^-1', 5.7e-7)
ideal_gas_constant = (8.314472, 'J mol^-1 K^-1', 1.5e-05)

#Consntats from Wikipedia
planck_constant_over_2_pi_in_J_s = (1.054571800e-34,'J s')
planck_constant_in_J_s = (6.626070040e-34, 'J s')
planck_constant_in_ev_s = (4.135667662e-15, 'eV s')

Temperature = float(sys.argv[2])



def getfreqsfromoutcar (outcar):
    """ This function returns a tuple where the first element contains a tuple with the lines in the OUTCAR file
    that contains the frequencies, the first element will have al the real frequencies, the second term contains
    all the frequencies incluiding the imaginary."""
    #outcar = os.path.abspath(sys.argv[1] and temperature is argument 2)


    read_lines_outcar = [line.strip('\n') for line in open(outcar, 'rb').readlines()]

    list_containing_all_frequencies = []
    list_containing_real_frequencies = []
    list_containg_imaginary_frquency = []

    for line in read_lines_outcar:
        if 'THz' in line :
            list_containing_all_frequencies.append(line.split())

        if 'THz'in line and not "f/i" in line:
            list_containing_real_frequencies.append(line.split())
        if 'f/i' in line:
            list_containg_imaginary_frquency.append(line.split())
    return list_containing_real_frequencies, list_containg_imaginary_frquency, list_containing_all_frequencies


Outcar_frequency_data_list = getfreqsfromoutcar(outcar=os.path.abspath(sys.argv[1]))[0]

Outcar_all_frequencies = getfreqsfromoutcar(outcar=os.path.abspath(sys.argv[1]))[2]



def energies_in_eV(tuple_with_energies_in_meV_from_outcar):
    """"""
    data_list_of_energies_in_meV = []
    for i in tuple_with_energies_in_meV_from_outcar:
        data_list_of_energies_in_meV.append(i[-2])
        data_list_of_energies_in_eV = map(lambda freq: float(freq)*1e-3, data_list_of_energies_in_meV)

    return data_list_of_energies_in_eV

energies_in_eV(Outcar_frequency_data_list) # calls the function on the Outcar

def frecuencies_in_wavenumber(tuple_with_frequencies):
    """This function takes  a tuple that contains the elements of the lines in the OUTCAR file
    where the frequencies are written. This frequencies are of the str type, therefore here they are converted to
    float type. Returns a list of frequencies in cm^-1 """
    data_list_of_frequencies = []
    for i in tuple_with_frequencies:
        data_list_of_frequencies.append(i[-4])
        data_list_of_frequencies_wavenumber = map(lambda freq: float(freq), data_list_of_frequencies)

    return data_list_of_frequencies_wavenumber



def zero_point_energy(tuple_frecuencies_in_wavenumbers):
    '''Returns the zero point energy based on the Harmonic Oscillator. E = 0.5 * planksconstant * frecuency.
    Since every mode is modeled with the harmonic oscillator, then the ZPE will be the sum of all the ZPEnergiess of the individual oscillators.
    Also, hbar * angular frecuency  would be the same as h * frecuency, because angular-frequency is
    2pi * frequency.
    The input is a list of  frequencies in cm^-1 and E =  h * v, where v is c/lambda
    Returns: the energies as in 0.5 * h * c * frequency '''

    sum_of_frequencies = 0.0

    for frequency in tuple_frecuencies_in_wavenumbers:
        sum_of_frequencies += frequency

    return 0.5* planck_constant_in_ev_s[0]*speed_of_light_in_vacuum[0]*100* sum_of_frequencies




def frequencies_to_energies_in_eV(tuple_frequencies_in_wavenumber):
    '''Returns a list of energies in eV from the frequencies_in_wavenumbers
    Conversion factor ->8065.54 wavenumber = 1 eV'''
    converstion_factor_wavenumber_to_eV = (8065.54, 'cm^-1') #BE CAREFUL WITH CONVERSION FACTORS
    return map(lambda freq: freq/(converstion_factor_wavenumber_to_eV[0]), tuple_frequencies_in_wavenumber)



def vibrational_entropy(temperature, vibrational_energies_in_eV):
    '''Calculates the entropy from vibrational contributions at a given temperature (K) and
    list of vibrational_energies in eV.
    Returns the entropy in ev/K.
    It assumes that the number of vibrational_energies have  3*N modes  ( n = number of atoms of the adsorbate)
    Reference: (1) Fultz, B. Vibrational Thermodynamics of Materials. 2009.
    '''

    temperature = Temperature
    Beta = 1/(boltzmann_constant_eV_per_K[0]*temperature) # edited, from t= 300 to t= variable

    entropy_vib = 0.0



    for ei in vibrational_energies_in_eV:
        entropy_vib += -np.log(1. - np.exp(-Beta*ei)) + (Beta*ei)/(np.exp(Beta*ei) - 1.)

    return boltzmann_constant_eV_per_K[0]* entropy_vib

energiesEv= frequencies_to_energies_in_eV(frecuencies_in_wavenumber(Outcar_frequency_data_list))
'''
test
if energiesEv == energies_in_eV(Outcar_frequency_data_list):
    print "energy lists are equal "
else:
    print"ERROR, energies not equal!!"
    print "first energiesEv from OUTCAR list", energiesEv
    print "second energies eV converted", energies_in_eV(Outcar_frequency_data_list)
'''



def _vibrational_entropy_contribution(energies, temperature): # function taken from ase.thermochemistry
        """Calculates the entropy due to vibrations for a set of vibrations
        given in eV and a temperature given in Kelvin.  Returns the entropy
        in eV/K."""
        temperature = Temperature
        kT = boltzmann_constant_eV_per_K[0]* temperature
        S_v = 0.
        for energy in energies:
            x = energy / kT
            S_v += x / (np.exp(x) - 1.) - np.log(1. - np.exp(-x))
        S_v *= boltzmann_constant_eV_per_K[0]
        return S_v


def get_ZPE_correction(energies):
        """Returns the zero-point vibrational energy correction in eV."""
        zpe = 0.
        for energy in energies:
            zpe += 0.5 * energy
        return zpe



ZPE = zero_point_energy(frecuencies_in_wavenumber(Outcar_frequency_data_list))
Svib = vibrational_entropy(temperature=Temperature, vibrational_energies_in_eV=frequencies_to_energies_in_eV(frecuencies_in_wavenumber(Outcar_frequency_data_list)))
TS = Svib*Temperature

ZPE_i = zero_point_energy(frecuencies_in_wavenumber(Outcar_all_frequencies))
TS_i = Temperature*_vibrational_entropy_contribution(energies_in_eV(Outcar_all_frequencies), Temperature)


print "zero point energy (ZPE):", round(zero_point_energy(frecuencies_in_wavenumber(Outcar_frequency_data_list)), 8), 'eV'

print "Svib my function  eV/K:", vibrational_entropy(temperature=Temperature,
                                                   vibrational_energies_in_eV=frequencies_to_energies_in_eV(frecuencies_in_wavenumber(Outcar_frequency_data_list)))
print "T*Svib MF eV:          ", TS, '\n'

print "ZPE from ASE:          ", get_ZPE_correction(energies_in_eV(Outcar_frequency_data_list)), '\n'

print'Svib form ASE.thermochemstry function:', _vibrational_entropy_contribution(energies_in_eV(Outcar_frequency_data_list),Temperature), '\n'
print "T*Svib ASE       :", Temperature* _vibrational_entropy_contribution(energies_in_eV(Outcar_frequency_data_list),Temperature)


print"-------------------"
print"ZPE including imaginary frequencies:", round(ZPE_i,5)

print"TS including imaginary frequencies:", round(TS_i,5)

######OUTPUTS FROM THIS SCRIPT###
f = open('frequencies_wavenumber.dat','w')
print >> f, frecuencies_in_wavenumber(Outcar_frequency_data_list), ', [cm^-1]'
f.close()
f2 = open('Thermochemistry.txt', 'w')
print >> f2, "Thermochemical corrections based on the harmonic oscillator\n" \
             "Reference:(1) Fultz, B. Vibrational Thermodynamics of Materials. 2009.\n" \
             "Reference:ASE.Thermochemistry class from the python package ASE"
print>> f2,"                        "
print>> f2,"                        "
print>> f2,"                        "
print>> f2,"Temperature             ", round(Temperature,2),"K"
print>> f2,"                        "
print>> f2,"ZPE                     ", round(ZPE, 3),"      eV"
print>> f2,"                        "
print>> f2,"Svib                    ", round(Svib,3),'      eV/K'
print>> f2,"                        "
print>> f2,"TS                      ", round(TS,3),"        eV"
print>> f2,"                        "
print>> f2,"                        "
print>> f2,"!"," ",round(ZPE, 5),"               ", round(TS,5)
print>> f2,"                        "
print>> f2,"                        "
print>> f2,"-------including imaginary freqs if any, below------------",
print>> f2,"                        "
print>> f2,"i ZPE                   ", round(ZPE_i,5)
print>> f2,"i TS                    ", round(TS_i,5)
print>> f2,"                        "
print>> f2,"                        "
print>> f2,"f/i"," ",round(ZPE_i, 5),"               ", round(TS_i,5)

f2.close()

