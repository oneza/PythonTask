import glob
import csv
import vtk
import numpy as np
from vtk.util import numpy_support
from dolfin import *
from matplotlib import *
from pylab import *

x=[[-15.9948,-259.567,46.0585],[19.2173,-259.134,41.1639],[60.3139,-269.595,7.38224],[92.6717,-265.316,-12.0567],[128.634,-241.675,-39.9371],[160.609,-189.953,-37.2119]]
n=len(x)
id=[]
k=0
def locator(filename):
    vtk_reader = vtk.vtkXMLUnstructuredGridReader()
    vtk_reader.SetFileName(filename)
    vtk_reader.Update()
    grid = vtk_reader.GetOutput()
    kdtree = vtk.vtkKdTreePointLocator()
    kdtree.SetDataSet(grid)
    kdtree.BuildLocator()
    time = numpy_support.vtk_to_numpy(grid.GetPointData().GetScalars())
    return kdtree,time
i=0
while i<n:
    kdtree,time=locator('solution000000.vtu')
    id.append(kdtree.FindClosestPoint(x[i]))
    i+=1
with open('forECG.csv', mode='w') as csv_file:
     writer = csv.DictWriter(csv_file, fieldnames=id)
     writer.writeheader()
for filename in sorted(glob.iglob('solution*.vtu')):
    kdtree,time=locator(filename)
    i=0
    PD=[]
    while i<n:
        PD.append(time[id[i]])
        i+=1
    with open('forECG.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(PD)
    k+=1
m=[]
i=0
while i<n:
    plt.subplot(3, 2, (i+1))
    a = np.loadtxt('forECG.csv', delimiter=',', skiprows=1, usecols=[i], unpack=True)
    m.append(max(a))
    plt.plot(np.arange(len(a)),a)
    i+=1
savefig("ecg_eq.png",dpi=None)
with open('./amplitude.csv', mode='a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(m)