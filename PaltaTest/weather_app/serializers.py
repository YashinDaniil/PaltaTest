from rest_framework import serializers


class WeatherCitySerializer(serializers.Serializer):
    city = serializers.CharField()


class RevokeSerializer(serializers.Serializer):
    task_id = serializers.IntegerField()