from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from PaltaTest.celery import app
from .services_api.weather_api import WeatherApi
from .models import Weather, Clients


@app.task
def create_task(lat, lon, user_id):
    client = Clients.objects.get(user_id=user_id)
    weather_data = WeatherApi().get_weather(lat, lon)

    w = Weather(
        client_id=client.id,
        city=weather_data['info_name'],
        date_time=weather_data['now_dt'],
        fact_temp=weather_data['fact_temp'],
        info_feels=weather_data['info_feels']
    )
    w.save()
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('events', {
        'type': 'events.alarm',
        'content': {
            'name': weather_data['now_dt'],
            'Температура': weather_data['fact_temp'],
            'Ощущается как': weather_data['info_feels']
        },
        'channel_name': client.channel_name
    })



