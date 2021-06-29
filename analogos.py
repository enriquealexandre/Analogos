import numpy as np

def analogos(x: np.ndarray, Train: np.ndarray, Test: np.ndarray) -> np.ndarray:
    #x: Lista con las variables que se van a tener en cuenta en el método
    #Train: Matriz con los datos de entrenamiento
    #Test: Matriz con los datos de validación
    #Salida: Matriz con los errores para cada punto

    E = np.empty_like(Train)
    for i in range(0,Test.shape[1]):
        Tr = np.squeeze(Train[x,:])        
        M = np.absolute(Tr - np.multiply(np.asmatrix(Test[x,i]).T,np.ones((1,Train.shape[1]))))
        m = np.sum(M,0)
        p = np.argsort(m)
        E[:,i] = 0.5*(Train[:,p[0,0]]+Train[:,p[0,1]])
    return E

        