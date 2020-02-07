# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:10:51 2020

@author: MF
"""
import requests
import json
appid="9b0bdf42a1a5e4bf2165ef07e9f950be"
url="http://api.openweathermap.org/data/2.5/weather?"
metric='metric'
while True:
    q=input("Enter City : ")
    if q =='q':
        break
    params={
        'appid':appid,
        'q':q,'units':metric}
    res=requests.get(url,params=params)
    res=json.loads(res.text)
    print(res['main']['temp'])

