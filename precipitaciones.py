import pygrib
import numpy as np

data = dict()
gr = pygrib.open('precipitaciones.grib')
for grb in gr:
    if grb.validDate.date() not in data:
        data[grb.validDate.date()] = grb.values
    else:
        data[grb.validDate.date()] += grb.values

datos = np.array([0,0])
for k,v in data.items():
    aux = np.array([k,v])
    datos = np.vstack((datos, aux))

import pandas
Tdf = pandas.DataFrame(datos)
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
from openpyxl.utils.dataframe import dataframe_to_rows
for r in dataframe_to_rows(Tdf, index=False, header=False):
    ws.append(r)
wb.save("precipitaciones.xlsx")