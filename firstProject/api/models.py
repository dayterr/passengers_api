from django.db import models


class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    travel_points = models.CharField(max_length=50)
