import requests
import json
from decouple import config


class WeatherApi:

    api_key = config('YANDEX_API_TOKEN')
    headers = {'X-Yandex-API-Key': api_key}

    def get_weather(self, lat, lon):
        payload = {
            'lat': lat,
            'lon': lon,
            'extra': False
        }
        r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers=self.headers)
        data = json.loads(r.text)

        return {
            'now': data['now'],
            'now_dt': data['now_dt'],
            'info_name': data['geo_object']['locality']['name'],
            'fact_temp': data['fact']['temp'],
            'info_feels': data['fact']['feels_like'],
        }
