import pygrib
import numpy as np

#Abro el fichero de datos
file = 'download.grib'
gr = pygrib.open(file)


#Me quedo únicamente con los valores de temperatura para un punto (Madrid, en concreto)
i=0
temp = np.empty([gr.messages,1])
for g in gr:
    temp[i] = g.values[138,95]-273.5 #Paso de K a C
    i=i+1
    
#Normalizo los datos a media cero y varianza unidad.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(temp)
temp = scaler.transform(temp)

#Para predecir un valor de temperatura voy a utilizar los N valores anteriores
#Organizo los datos en dos matrices:
# _x: Son los datos de entrada. Las filas contienen los N valores utilizados para predecir, y cada columna es un instante temporal
# _y: Son los targets. Cada valor es el valor que habría que predecir. 
N=12   #Ventana de predicción
temp_x = np.empty([temp.size-N,N])
for i in range(0,temp.size-N):
    temp_x[i,] = temp[i:i+N,0]
temp_y = temp[N:]

#Entreno con los primeros 30 años y testeo con los restantes
temp_train_x = temp_x[0:360,:]
temp_train_y = temp_y[0:360]
temp_test_x = temp_x[360:]
temp_test_y = temp_y[360:]


#Generación de la ELM (está sin ajustar)
from random_layer import RandomLayer
from sklearn.linear_model import Ridge
from sklearn import pipeline

n_hidden = 50   
alpha = 0.7
rbf_width = 0.1
activation_func = 'sigmoid'
regressor = None
random_state = 0
ridge_alpha = 0.001
rl = RandomLayer( n_hidden = n_hidden, alpha = alpha, 
    rbf_width = rbf_width, activation_func = activation_func )

ridge = Ridge( alpha = ridge_alpha )

elmr = pipeline.Pipeline( [( 'rl', rl ), ( 'ridge', ridge )] )  

#Entreno la ELM
elmr.fit(temp_train_x, temp_train_y)
print ("ELM: Training Score: ",elmr.score(temp_train_x, temp_train_y)," - Testing Score: ", elmr.score(temp_test_x, temp_test_y))

#Visualizo el resultado
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(temp_y) 
plt.plot(elmr.predict(temp_x), 'r')
plt.title('Resultado con una ELM')

###########################################
###########################################
#Voy a probar con una SVM, a ver qué tal va
from sklearn import svm
regr = svm.SVR()
regr.fit(temp_train_x, np.ravel(temp_train_y))

print ("SVM: Training Score: ",regr.score(temp_train_x, temp_train_y)," - Testing Score: ", regr.score(temp_test_x, temp_test_y))
plt.figure(2)
plt.plot(temp_y)
plt.plot(regr.predict(temp_x),'r')
plt.title('Resultado con una SVM')
plt.show()
