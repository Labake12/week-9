import requests

url = 'https://localhost:5000/ping'
res = requests.post(url, json={'text': 'I liked the movie'})
print(res.text)