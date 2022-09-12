import adhoc_thermodynamic as thermo
import sys
import numpy as np

""" This script uses the module adhoc_thermodynamic script. It allows you to choose the number of vibrational modes based on the geomery of the molecule to get the entropy corrections.
USAGE: 
python nameof script OUTCAR temperature <geometry: (liner, non-linear) or choose > < nofatoms or number of wanted freqs> 
TO DO: add usage to the program from terminal
"""

#variables:
geometry = str(sys.argv[3] )
nofatoms_or_nfreqs = int( sys.argv[4] )


freqsfromoutcar = thermo.Outcar_frequency_data_list
temperature = thermo.Temperature
freqsin_w = thermo.frecuencies_in_wavenumber(freqsfromoutcar)
print "freqs in w", freqsin_w

freqs_in_eV= thermo.frequencies_to_energies_in_eV(freqsin_w)
print "freqs in eV", freqs_in_eV

numberofvibmodes = thermo.get_num_vib_modes( geometry,nofatoms_or_nfreqs )

finalfreqs=freqs_in_eV[:numberofvibmodes]

"""
#this if statement is not nessesary

finalfreqs = 0
if 'choose' in geometry:
    finalfreqs = freqs_in_eV[:numberofvibmodes]
else:
    finalfreqs = freqs_in_eV[:numberofvibmodes]
"""

ZPE = thermo.get_ZPE_correction_eV(finalfreqs)
Svib = thermo.vibrational_entropy(temperature, finalfreqs)
TS = temperature* Svib

print "number of freqs:" , numberofvibmodes
print" final freqs" , finalfreqs
print "zpe from thermoGeom", thermo.get_ZPE_correction_eV( finalfreqs )
print "  Svib from thermo with Geometry", '{:0.2e}'.format(Svib) # rounded  output will be in scientific notation
print"temereature used:", temperature

file = open('Thermo_moleculeGeom.txt', 'w' )


print >> file, "Thermochemical corrections based on the harmonic oscillator\n" \
             "Reference:(1) Fultz, B. Vibrational Thermodynamics of Materials. 2009.\n" \
             "Reference:ASE.Thermochemistry class from the python package ASE"
print>> file,"                        "
print>> file,"                        "
print>> file,"                        "
print>> file,"Temperature             ", round(temperature,2),"K"
print>> file,"                        "
print>> file,"                        "
print>> file,"                        "
print>> file,"ZPE                     ", round(ZPE, 2),"      eV"
print>> file,"                        "
print>> file,"Svib                    ", '{:0.2e}'.format(Svib),"          eV/K"
print>> file,"                        "
print>> file,"TS                      ", '{:0.2e}'.format(TS),"             eV"
print>> file,"                        "
print>> file,"                        "
print>> file,"                        "
print>> file,"number of freqs:        ", numberofvibmodes
print>> file,"freqs used              ", finalfreqs



file.close()

