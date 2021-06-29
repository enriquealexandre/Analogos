import numpy as np
import pandas
from analogos import analogos
#import openpyxl
#from openpyxl.utils.dataframe import dataframe_to_rows

#Para hacer pruebas leo datos de Viento de ECA
#Están organizados de modo que son matrices NxM, donde N es el número de variables y M el número de instantes de tiempo.
aux = pandas.read_excel("Train.xls",header=None)
Train = aux.to_numpy()
aux = pandas.read_excel("Test.xls",header=None)
Test = aux.to_numpy()
aux = pandas.read_excel("best.xls",header=None)
x = aux.to_numpy()
x = x-1  #Esto es porque los valores de x están en formato Matlab (el primer índice es 0)

#Método de los análogos
e = analogos(x,Train,Test)
print("Error: ", e)

#Exporto los datos a Excel
#Tdf = pandas.DataFrame(E)
#wb = openpyxl.Workbook()
#ws = wb.active

#for r in dataframe_to_rows(Tdf, index=False, header=False):

#    ws.append(r)
#wb.save("salida.xlsx")