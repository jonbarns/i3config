#!/usr/bin/python3

import requests
import json

URL = 'https://api.openweathermap.org/data/2.5/weather?id=3333123&units=metric&appid=d246e9381121f746eda835f525a1660f'

GLYPHS = {
    'clear'         : '',
    'clouds'        : '',
    'rain'          : '',
    'drizzle'       : '',
    'thunderstorm'  : '',
    'snow'          : '',
    'atmosphere'    : '',
    }

def save_data():
    weather_data=requests.get(URL).json()
    with open('data.txt', 'w') as file:
        json.dump(weather_data, file)

def main():
    weather_data=requests.get(URL).json() 
    temperature = weather_data['main']['temp']
    current_condition = weather_data['weather'][0]['main'].lower()
 
    for glyph, icon in GLYPHS.items():
        if glyph in current_condition:
            current_icon = icon
    
    full_text = f"{current_icon} {str(temperature):{1}.{4}} \u2070C"
    short_text = f"{current_icon} {str(temperature):{1}.{2}} \u2070C"

    print(f"{full_text}")
    print(f"{short_text}")

if __name__ == '__main__':
    main()
