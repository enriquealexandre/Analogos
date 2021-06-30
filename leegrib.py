import pygrib
import numpy as np

#Leo el fichero .grib y extraigo las temperaturas para Madrid

file = 'download.grib'
gr = pygrib.open(file)

i=0
temp = np.empty(gr.messages)
for g in gr:
    temp[i] = g.values[138,95]-273.5 #Paso de K a C
    i=i+1
    
print(temp)

