from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/weather/', include('weather_app.urls')),
]
