from django.db import models


class Events(models.Model):
    class Meta:
        db_table = "Events"

    event_id = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    rank = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self) -> str:
        return self.title + str(self.rank)


class EventCountry(models.Model):
    class Meta:
        db_table = "EventCountry"

    event = models.ForeignKey(to=Events, on_delete=models.CASCADE)
    country = models.CharField(max_length=10)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.country


class Weather(models.Model):
    class Meta:
        db_table = "Weather"

    event = models.ForeignKey(to=Events, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.IntegerField()

    def __str__(self) -> str:
        return str(self.temperature) + ", " + str(self.humidity)


class Flights(models.Model):
    class Meta:
        db_table = "Flights"

    event = models.ForeignKey(to=Events, on_delete=models.CASCADE)
