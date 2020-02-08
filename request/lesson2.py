# -*- coding: utf-8 -*-
import requests

response = requests.get('https://reqres.in/api/users')
dic = response.json()

for i in range(len(dic["data"])):
    print(dic["data"][i]['email'])