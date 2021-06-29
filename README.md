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


