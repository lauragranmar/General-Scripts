#! /usr/bin/env python
import numpy as np
import matplotlib as mpl
mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import sys

#This script is a modified version of vaspkit scripts for plotting the DOS. ( https://doi.org/10.1016/j.cpc.2021.108033 ) 
# I have added the normalize function and changed some code.
#------------------ Functions ----------------------

#use to normalized the y axis using  y' = a + (y-ymin)(b-a)/y.max-y.min  where a , b is the range you want the scale to be.
def normalize(datarange):
    """this takes the passed data and normalize it in the range [a,b]
    """
    #y_norm = (datarange - np.min(datarange)) / np.ptp(datarange) #(np.max(datarange)- np.min(datarange))
    y_norm =  (datarange-np.min(datarange)) / (np.max(datarange)-np.min(datarange)) #np.ptp(datarange)
    return np.nan_to_num(y_norm) # this convert NAN values to zero. If there are any.


#------------------ FONT_setup ----------------------
font = {'family' : 'arial',
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 20.0,
    }

#------------------- Data Read ----------------------
pdosfile=sys.argv[1]

with open(pdosfile,"r") as reader:
    legend = reader.readline()
legends=legend.split()[1:] #omits the 0th label
legends=[i.replace("_"," ") for i in legends]
legend_s=tuple(legends)
datas = np.loadtxt(pdosfile,dtype=np.float64,skiprows=1)

datanorm = normalize(datas) # normalize the Y axis the orbitals

#--------------------- PLOTs ------------------------
axe = plt.subplot(111)
# Color methods! choose only one of the two methods


axe.plot(datas[:,0], datanorm[:,1:],linewidth=1.5) #auto colors
#axe.fill_between(datas[:,0], datanorm[:,8].min(), datanorm[:,8], facecolor='orange', alpha=0.5,linestyle='-' )
#axe.plot(datas[:,0],datas[:,1:],linewidth=1.0) #auto colors



axe.set_xlabel(r'${E}$-$E_{f}$ (eV)',fontdict=font)
axe.set_ylabel(r'PDOS (states/eV)',fontdict=font)
plt.yticks(fontsize=font['size']-2,fontname=font['family'])
plt.xticks(fontsize=font['size']-2,fontname=font['family'])
plt.legend(legend_s,loc='best', frameon=False)
plt.xlim(( -10,  10)) # set y limits manually
axe.axvline(x=0, color='k',linestyle='--',linewidth=1.5)
span= 0.5
axe.xaxis.set_ticks(np.arange(-10,10, span), minor=True)
axe.tick_params(axis='both',  right=True, top= True, which='both', direction='in', width=2, size=5)

#axe.axhline(y=0, color='k',linestyle='--',linewidth=1.5)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize=font['size'])
fig = plt.gcf()
fig.set_size_inches( 8, 6)
name = pdosfile
plt.savefig(name+'.png', dpi= 300, format='png', transparent=True, style='presentation')
#plt.savefig("testarray2.png", dpi= 300, format='png', transparent=True, style='presentation')

