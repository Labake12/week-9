import requests

url = 'https://0206-102-89-33-92.ngrok-free.app/predict'
res = requests.post(url, json={'text': 'I liked the movie'})
print(res.text)