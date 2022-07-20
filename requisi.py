import requests
import json

r = input("Insira o termo de busca: ")
s = requests.get('https://google.com/search?q=' + r)
if s.status_code == 200:
  print(s.url)

  
