import pygrib
import numpy as np

data = dict()
gr = pygrib.open('temperaturas.grib')
for grb in gr:
    if grb.validDate.date() not in data:
        data[grb.validDate.date()] = np.zeros((1,24))
        data[grb.validDate.date()][0,grb.validDate.time().hour] = grb.values-273.15
    else:
        data[grb.validDate.date()][0,grb.validDate.time().hour] = grb.values-273.15

datos = np.array(["fecha", 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23, "min", "max", "media"])
for k,v in data.items():
    aux = np.empty((1,28),dtype=object)
    aux[0,0] = k
    aux[0,1:25] = v
    aux[0,25] = np.min(v)
    aux[0,26] = np.max(v)
    aux[0,27] = np.mean(v)
    datos = np.vstack((datos, np.squeeze(aux)))

import pandas
Tdf = pandas.DataFrame(datos)
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
from openpyxl.utils.dataframe import dataframe_to_rows
for r in dataframe_to_rows(Tdf, index=False, header=False):
    ws.append(r)
wb.save("temperaturas.xlsx")