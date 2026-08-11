import requests
import json 
response = requests.get(" https://api.thecatapi.com/v1/breeds/")
datos = response.json()


print(f"{'Nombre':<25} {'origin':<20} {'wikipedia_url'}")

for gato in datos[:13]:
    print(
        f"{gato['name']:<25} "
        f"{gato['origin']:<20} "
        f"{gato['wikipedia_url']}"
 )


response1  = requests.get("https://randomuser.me/api/?results=20") 
datos1 = response1.json()

Nombres = []
for i in range (20):
    Nombres.append(datos1['results'][i]['name']['first'] + " " + datos1['results'][i]['name']['last'] )

print (Nombres)