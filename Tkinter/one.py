import requests

res = requests.get('http://localhost:9090/api/v1/todos')

print(res.text)