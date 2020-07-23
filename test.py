import requests

BASE = "http://127.0.0.1:5000/"

data = [{'likes':20, 'name':'Lollo', 'views':123},
        {'likes':4, 'name':'Pillo', 'views':45},
        {'likes':204, 'name':'Calo', 'views':235}]
for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + 'video/2')
print(response.json())