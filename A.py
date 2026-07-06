import requests
response = requests.get("https://randomuser.me/api/?results=20")
list = []
for i in range(20):
    list.append(response.json()['results'][i]['name']['first'] + "" + response.json()['results'][i]['name']['last'])

print(list)