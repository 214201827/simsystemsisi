# Importación de librerías necesarias

import pandas as pd
import matplotlib.pyplot as mp
from sklearn import linear_model

# Cargar datos

data = {'Edad': [25, 30, 35, 40, 45],
        'Salario': [3000, 3500, 4000, 4500, 5000]}

df = pd.DataFrame(data)





# Prueba de carga de datos

print(df)




# Carga de series y prueba de carga

serie_x = df[["Edad"]]
serie_y = df[["Salario"]]

#print(serie_x)
#print(serie_y)

mp.scatter(serie_x, serie_y)

# Modificadores

mp.xlabel("Edad")





model = linear_model.LinearRegression()

model.fit(serie_x, serie_y)
