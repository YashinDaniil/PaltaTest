import uuid
from django.db import models


class Clients(models.Model):
    channel_name = models.CharField(max_length=255, null=True)
    user_id = models.UUIDField(default=uuid.uuid4())

    class Meta:
        db_table = 'clients'


class Weather(models.Model):
    city = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    fact_temp = models.IntegerField()
    info_feels = models.IntegerField()
    client = models.ForeignKey(Clients, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'weather'
