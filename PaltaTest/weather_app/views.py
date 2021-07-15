import json
import random
import string

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from decouple import config
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Clients, Weather
from .services_api.geocoder_api import Geokoder
from .serializers import WeatherCitySerializer, RevokeSerializer
from rest_framework.permissions import AllowAny
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class SetPosition(generics.GenericAPIView):
    serializer_class = WeatherCitySerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(Clients, user_id=request.headers.get('User_ID'))
        geo_data = Geokoder().get_geo(serializer.data['city'])

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=config('CELERY_WORKER_TIMEOUT', default=300, cast=int),
            period=IntervalSchedule.SECONDS,
        )
        task_name = serializer.data['city'] + str(user.user_id) + ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
        a = PeriodicTask.objects.create(
            interval=schedule,
            name=task_name,
            task='weather_app.tasks.create_task',  # name of task.
            args=json.dumps([geo_data['geo_lat'], geo_data['geo_lon'], str(user.user_id)]),
        )
        return Response(data={'task_id': a.id}, status=202)


class RevokeTask(generics.GenericAPIView):
    serializer_class = RevokeSerializer
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = self.get_serializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        PeriodicTask.objects.get(pk=serializer.data['task_id']).delete()
        return Response(status=status.HTTP_200_OK)


class GetOldSearch(generics.GenericAPIView):
    def get(self, request, user_id):
        client = get_object_or_404(Clients, user_id=user_id)
        req = Weather.objects.filter(client=client)
        resp_data = {}
        for i in req:
            if i.city not in resp_data.keys():
                resp_data[i.city] = []
            resp_data[i.city].append(
                {
                    'name': i.date_time,
                    'Температура': i.fact_temp,
                    'Ощущается как': i.info_feels,
                }
            )

        return Response(resp_data)
