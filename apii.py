import json
import requests


class Sel_Country:

    def __init__(self, country):
        self.country = country
        self.city = []

    def selection(self):
        '''
        выбирает города из станы self.country
        :return: список городов
        '''
        with open('city.list.json', 'r') as file:
             date = json.load(file)
        for i in date:
            if i['country'] == self.country:
                self.city.append(i['name'])
        self.city.sort()
        return self.city

    def cities(self, city):
        '''
        обращаемся к API (openweather)
        :return: температуру и скорость ветра
        '''
        weather_city = []
        temp_wind = [('main', 'temp'), ('wind', 'speed')] # список погодных условий
        url_api = 'https://api.openweathermap.org/data/2.5/weather'
        par = {
            'q': city,
            'units': 'Metric',
            'appid': '59de847352eb3fc82bc64211e6d259d2'
        }
        response = requests.get(url_api, params=par)
        weather = response.json()
        for i, a in temp_wind:
            weather_city.append(weather[i][a])
        return weather_city


