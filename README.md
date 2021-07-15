# Тестовое задание 

Сервер для проверки: http://92.255.198.180/

```
>> git clone
>> cd
>> docker-compose build
>> docker-compose run backend python ./PaltaTest/manage.py migrate weather_app --noinput
>> docker-compose run backend python ./PaltaTest/manage.py migrate django_celery_beat --noinput
>> docker-compose up
```