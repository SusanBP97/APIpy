import requests
response = requests.get("https://randomuser.me/api/?results=20")
name = []
email = []
country = []
age = []
country_code = []
age_code_max = []
age_code_min = []

for i in range(20):
    name.append(response.json()['results'][i]['name']['first'] + " " + response.json()['results'][i]['name']['last'])
    email.append(response.json()['results'][i]['email'])
    country.append(response.json()['results'][i]['location']['country'])
    age.append(response.json()['results'][i]['dob']['age'])
 

for i in range(len(age)):
     if age[i] > 30:
         age_code_max.append((name[i], email[i], country[i], age[i]))
     else:
         age_code_min.append((name[i], email[i], country[i], age[i]))


