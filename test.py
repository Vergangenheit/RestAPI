import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.put(BASE + 'video/1', {'likes':20, 'name':'Lollo', 'views':123})
# print(response.json())
# input()
response = requests.get(BASE + 'video/6')
print(response.json())