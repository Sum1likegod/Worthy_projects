import requests
import pyttsx3
import json
import os

city = input("enter city name you want to know the weather of ")

url = f"https://api.weatherapi.com/v1/current.json?key=086886e7a58c497695552215240606&q={city}"

r = requests.get(url)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

aud = pyttsx3.init()

aud.say(f"The current weather in {city} is {w}")
print(f"The current weather in {city} is {w}")

aud.runAndWait()
