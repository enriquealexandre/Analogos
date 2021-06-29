import numpy as np

def analogos(x: np.ndarray, Train: np.ndarray, Test: np.ndarray) -> float:
    #x: Lista con las variables que se van a tener en cuenta en el método
    #Train: Matriz con los datos de entrenamiento
    #Test: Matriz con los datos de validación
    #Salida: Matriz con los errores para cada punto

    E = np.empty_like(Train)
    T = np.empty_like(Train)
    for i in range(0,Test.shape[1]):
        Tr = np.squeeze(Train[x,:])        
        # Para cada instante de tiempo cogemos los puntos que más se parecen en el pasado:
        M = np.absolute(Tr - np.multiply(np.asmatrix(Test[x,i]).T,np.ones((1,Train.shape[1]))))
        #Calculo el parecido para todos los puntos
        m = np.sum(M,0)
        p = np.argsort(m)
        #Promedio en los dos instantes de tiempo más parecidos
        T[:,i] = 0.5*(Train[:,p[0,0]]+Train[:,p[0,1]])
        #Calculo el error al reconstruir toda la matriz con esos dos puntos
        E[:,i] = np.sum(np.square(T[:,i] - Test[:,i]))
    f = np.sum(E)/E.size

    return f 


