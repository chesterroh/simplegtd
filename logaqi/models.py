from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateTimeField('created date')
    def __str__(self):
        return self.name

class Aqidata(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    temp = models.FloatField(default=0)
    humid = models.FloatField(default=0)
    aqi01 = models.FloatField(default=0)
    aqi25 = models.FloatField(default=0)
    aqi10 = models.FloatField(default=0)
    voc = models.FloatField(default=0)
    co2 = models.FloatField(default=0)
    log_date = models.DateTimeField('logging datetime')
