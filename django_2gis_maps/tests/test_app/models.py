from django.db import models
from django_2gis_maps.fields import AddressField, GeoLocationField


class Person(models.Model):
    address = AddressField(max_length=100)
    geolocation = GeoLocationField(blank=True)
