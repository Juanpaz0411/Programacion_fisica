import pandas as pd
import numpy as np

# serie = pd.Series([1,2,3])

# #print(dir(pd))

# serie.name='nombre'

# print(serie)

# df = pd.DataFrame({'columna1':[1,2,3,4], 'columna2': ['a','b','c','d']})
# print(df)

# print(df.shape)#tamaño del dataframe

# db = pd.read_csv(r"C:\Users\USUARIO WINDOWS\programacion\estudio\pandas\Libro_1.csv", sep=";")
# print(db) #accede a dataframe a veces se agrega <header=None>

# df = pd.read_csv(r"C:\Users\USUARIO WINDOWS\programacion\estudio\pandas\exo_2.csv", sep=",")
# print(df)

# df = pd.read_csv(r"C:\Users\USUARIO WINDOWS\programacion\estudio\pandas\exo_2.csv", sep=",")
# print(df)#agregar <head=None> indica que no hay cabeceros

# print(df.shape)#nos indica el tamaño del dataframe.

# print(df.head(3))#muestra las primeras filas que querramos, en este caso son tres filas

# print(df.tail(2))#muestra las ultimas filas que querramos, en este caso son dos

df = pd.read_csv(r"C:\Users\USUARIO WINDOWS\programacion\estudio\pandas\Libro_1.csv", sep=";")

nombres = ['nom','apellido', 'utilidad']

df.columns = nombres # cambia las columnas por los elementos de una tupla

# print (df.head(1))

# print(df.columns)#devuelve el nombre de las columnas

# print(df.index)#imprime los índices de las filas de un objeto DataFrame en pandas.
# print(df.describe())#datos estadisticos de cada columna
#print(df['nom'].value_counts())#en df['nombre de columna'], nos dice los casos de cada fila, y el tipo

#print(df.T)#transpone la 'matriz' o tabla dada

# print(df[['nom', 'apellido']])#toma las columnas seleccionadas o introducidas en la tupla
# print(df[['nom', 'apellido']].head(2))#toma las dos primeras filas

# print(df.iloc[[0,2]])#dice que filas queremos usando los indices de las filas 

# print(df.iloc[[0,2], [0,2]])#la primera tupla corresponde a las filas, la segunda a las columnas

# print(df)
# print(df[(df['utilidad']>5)])#filtra solo casos donde los valores de la columna sea mayor que 5
    #se puede seguir filtrando con &, es decir print(df[(df['utilidad']>5)&(df['nombre'],2)])
        #esto hace una dataframe aplicando los filtros



df = pd.read_csv(r"C:\Users\USUARIO WINDOWS\programacion\estudio\pandas\exo_2.csv", sep=",")
# print(df)

# print(df['Distance']-df['Gaia Magnitude'])#se restan los datos de dos columnas
# print(df.isna().sum())#nos dice que valores perdidos hay por columna
    #hay valores perdidos o valores que no tenemos disponibles
# print(df.isna().sum().sum())#numero total de datos perdidos por dataframe


df['Gaia Magnitude'][:2] = np.nan#toma las primeras dos columnas <0 y 1> y le cambia los datos por 
print(df['Gaia Magnitude'].head())

print(df['Gaia Magnitude'])#imprime una columna especifica