import requests
import json
import pandas as pd       
from pandas import json_normalize
import datetime
import config_inicial as config_inicial 

#Listas obtenidas para las ciudades y coordenadas
cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=51.5074&lon=-0.1278", "lat=40.7128&lon=-74.0060", "lat=-31.4197&lon=-64.1915", "lat=25.0330&lon=121.5654", "lat=-34.6037&lon=-58.3816", "lat=19.4326&lon=-99.1332", "lat=53.3498&lon=-6.2603", "lat=38.7223&lon=21.7632", "lat=4.7110&lon=-74.0721", "lat=35.6895&lon=139.6917"]

data=[]

#DEFINIMOS UNA FUNCION CON LOS PARAMETROS DE LAS CIUDADES Y COORDENADAS
def funcion_clima (city,coordList):
    if __name__== "__main__":
        #Declaramos  la URL, invocando la API_KEY y tomando los PARAMETROS 
        url= f'https://api.openweathermap.org/data/2.5/weather?{coordList}&appid={config_inicial.api_key}&units=metric'
        response= requests.get(url)

        #Verificamos si el status_code nos responde correctamente 
        if response.status_code == 200 :
            #Trae el contiene la api convertido en JSON con el metodo RESPONSE.JSON
            response_json= response.json()
        
           #Creo el diccionario pasandole los valores del json obtenido
            info = {
            "Ciudad":cityList,
            "city_id": response_json["id"],
            "longitude": response_json["coord"]["lon"],
            "latitude": response_json["coord"]["lat"],
            "temp": response_json["main"]["temp"],
            "temp_min": response_json["main"]["temp_min"],
            "temp_max": response_json["main"]["temp_max"],
            "pressure": response_json["main"]["pressure"],
            "humidity": response_json["main"]["humidity"]
            }
    
              
            # Cargo todos los valores de cada diccionario en una lista
            data.append(info)
            # Convertir la lista de diccionarios en un DataFrame
            df = pd.DataFrame(data)

            #Treamos la fecha actual con datatime.now y la formateamos con STRFTIME("formato que queremos")   
            fecha= datetime.datetime.now().strftime("%Y-%m-%d")
        
            text= "TiempoDiario_"
        
            #Creamos un solo csv con la funcion TO.CSV() de los datos meteorologico pasados como argumento.
            with open (f"data_analytics\openweather\{text}{fecha}.csv",'w') as output_file:
                df.to_csv(output_file,index=False)


        print(F"{text}{city} FUE CREADO CON EXITO")
    else:
        print(f"NO se creo {text}{city}")

#Creamos el for para iterar las listas de ciudades y coordenadas con el metodo ZIP, llamando a la funcion_clima
for (cityList,coordList) in zip(cityList,coordList):
    funcion_clima(cityList,coordList)
    
    

