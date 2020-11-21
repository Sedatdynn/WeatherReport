import requests
import json

api_key = "API_KEY"
base_url= "http://api.openweathermap.org/data/2.5/weather?"
il = input("Şehir : ") 
complete_url = base_url + "appid=" + api_key + "&q=" + il  
response = requests.get(complete_url) 
x = response.json() 

if x["cod"] != "404":
    y = x["main"]
    Sıcaklık = y["temp"]
    Basınc = y["pressure"] 
    Nem = y["humidity"] 
    z = x["weather"]  

    Hava_Durumu = z[0]["description"]

    print(f"Sıcaklık: {Sıcaklık - 273} *C\nBasınc: {Basınc} Pascal\nNem: % {Nem}\nHava durumu:{Hava_Durumu}")
    
else: 
    print(" City Not Found ")  

