import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
file_path='C:/Users/USER/Desktop/Practica_api/Proyecto_Nivel1/data_analytics/openweather/TiempoDiario_2023-08-16.csv'
clima= pd.read_csv(file_path)
print(clima)

print(clima.plot.bar())
#plot (Matplotlib ) nos grafica el pedido 


#Probamos con obteniendo un grafico con las  ubicaciones
clima.head(10).plot.bar()



#Creamos una nueva variable para solo los datos que queriamos obtener con mas precision
info = ['Ciudad','temp','temp_min','temp_max' ]

#La llamamos con la ubicacion 0 para que pueda traernos cada ubicacion con su nombre.
clima[info].plot.bar(0)
