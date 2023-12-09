import requests

url = 'https://fcae-102-89-32-179.ngrok-free.app/predict'
res = requests.post(url, json={'text': 'The movie is just bad'})
print(res.text)