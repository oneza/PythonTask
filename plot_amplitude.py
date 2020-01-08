import glob
import csv
import vtk
import numpy as np
from vtk.util import numpy_support
from dolfin import *
from matplotlib import *
from pylab import *

i=0
V=["V1","V2","V3","V4","V5","V6"]
while i<6:
    #plt.subplot(3, 2, (i+1))
    a = np.loadtxt('amplitude.csv', delimiter=',', usecols=[i], unpack=True)
    #plt.title(V[i])
    plt.plot(np.arange(len(a)),a, label=V[i], linewidth=3)
    xticks(np.arange(7), ('0.1i', '0.2i', '0.5i', 'i', '2i', '5i', '10i'))
    #plt.tight_layout()   
    i+=1
plt.grid(True)
plt.legend(loc='upper right')
plt.xlabel('Extracellular conductivity depending on intracellular conductivity (i)')
plt.ylabel('Amplitude, mV')
plt.tight_layout()
savefig("ecg_amplitude.png",dpi=640/8)