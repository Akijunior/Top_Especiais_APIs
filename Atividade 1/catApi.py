import requests
import random

api_key = "MzA0MDU1"
baseurl = 'http://thecatapi.com/api/images/get.php/'
cmd = ['format=xml', 'image_id=']
image_id = random.randint(1, 1000)
cmd[1] += str(image_id)
print(cmd[1])
urlgen = baseurl+cmd[0]+'&'+cmd[1]+'.php'
print(urlgen)

response = requests.get(urlgen)
json = response.json('')
