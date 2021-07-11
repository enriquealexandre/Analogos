# Código para hacer pruebas #

## Analogos.py ##
Este es el método de los análogos tal cual. 
El método viene descrito en: https://journals.ametsoc.org/view/journals/atsc/26/4/1520-0469_1969_26_636_aparbn_2_0_co_2.xml

El código toma a su entrada tres variables:
 - x: Es la lista de variables de entrada que se van a tener en cuenta. Está puesto por si en algún momento queremos probar a anular alguna variable de entrada o a hacer una selección. 
 - Train: Son los datos de entrenamiento. Tal cual está programado se considera que es una matriz en la que cada fila representa una variable de entrada y cada columna un instante temporal. 
 - Test: Son los datos de validación. 

 El algoritmo lo que hace es, para cada instante de tiempo de la matriz de validación, buscar los dos instantes temporales de la matriz de entrenamiento que tienen valores más parecidos. Con esos dos instantes, se promedia, y se reconstruye una "estimación" del valor de la matriz de Validación, que es el que se compara con el real y se calcula el error final. 


## download.py ##
Esto no es más que un script para bajarse los datos de temperatura del ERA. El procedimiento es más o menos este:
- Loguearse en https://cds.climate.copernicus.eu/user/login
- Copiar las dos líneas del cuadro negro en https://cds.climate.copernicus.eu/api-how-to
- touch ~/.cdsapirc
- Copiar esas dos líneas en .cdsapirc
- Instalar la  API para python: pip install cdsapi
- Para descargar datos: https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels-monthly-means?tab=form
- Para usar los archivos .grib: https://confluence.ecmwf.int/display/CKB/How+to+plot+GRIB+files+with+Python+and+matplotlib


## ga.py ##
Un algoritmo genético muy sencillo. Por ahora no sirve para nada, pero lo dejo aquí por si acaso. 

## test.py ##
Script para probar el método de los análogos. Por ahora lee los datos de los archivos Excel Train, Test y best, que son las exportaciones directas de los datos que tenía en Matlab, para comprobar que todo concuerda al traducir a Python. Habría que modificar eso para leer los datos directamente del archivo download.grib, que es el que se ha descargado de la web del ERA. 

## ELM ##
Este es el código fuente tal cual de la ELM (Extreme Learning Machine). Está bajado de https://www3.ntu.edu.sg/home/egbhuang/elm_codes.html

## download.grib (y leegrib.py) ##
Este archivo de datos es el que he descargado utilizando el código de download.py. Se trata de la temperatura media mensual desde 1979 para una rejilla de puntos en Europa. 
Para leer los datos se puede utilizar la librería pygrib

    import pygrib
    file = 'download.grib'
    gr = pygrib.open(file)

Con esto se tiene en la variable gr el archivo abierto. Esta variable es una lista con un montón de valores. Se pueden ver todos haciendo:
    for g in gr:
        print(g)

Salen 509 instantes de tiempo, desde enero de 1979 hasta mayo de 2021. Se puede ver que los valores que vamos a tener de temperatura vienen dados en grados Kelvin. 

Para acceder a los datos de uno de estos meses (por ejemplo, el primero):
    g = gr[1] #En este caso la numeración empieza en 1
    g.values

El comando g.values devuelve la matriz de temperaturas para todos los puntos de la rejilla en ese instante temporal. Se puede ver que la rejilla tiene 171x291 puntos (g.values.shape).
La latitud y longitud de cada uno de los puntos de la rejilla se pueden obtener haciendo:
    lats, lons = g.latlons()

Madrid, por ejemplo, estaría en los índices [138,95] (Latitud 40.5, Longitud -3.75)

## TestELM.py
Permite probar a realizar la predicción de una serie temporal utilizando una ELM (Extreme Learning Machine).
El código para ELMs está en la carpeta ELM, y está bajado de: https://personal.ntu.edu.sg/egbhuang/elm_codes.html
He adaptado el código de random_layer.py para adaptarlo a Python 3, porque daba algunos errores.
El código coge los datos de download.grib, que son una serie temporal de temperaturas medidas en una rejilla que cubre toda Europa. Me quedo sólo con un punto (más o menos cercano a Madrid), y esa es la serie temporal que utilizo para hacer pruebas. 
Se predice la muestra x en base a N muestras anteriores (N es configurable).
Al final también se hace la prueba con una SVM.

