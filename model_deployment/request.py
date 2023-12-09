import requests

url = 'https://localhost:5000/predict'
res = requests.post(url, json={'text': 'I liked the movie'})
print(res.text)