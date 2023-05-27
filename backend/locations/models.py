from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models


class Location(models.Model):
    city = models.CharField(verbose_name='City', max_length=70)
    state = models.CharField(verbose_name='State', max_length=70)
    zip = models.CharField(
        verbose_name='Zip Code',
        max_length=5,
        validators=[RegexValidator(r'^\d{5}$')],
        primary_key=True,
    )
    latitude = models.FloatField(
        verbose_name='Latitude',
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )
    longitude = models.FloatField(
        verbose_name='Longitude',
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )

    def __str__(self):
        return f'{self.city}, {self.state}, {self.zip}'

    def get_distance(self, location):
        """
        Return:
            The distance between this location and another location in miles.
        """
        from geopy.distance import distance
        return distance(
            (self.latitude, self.longitude),
            (location.latitude, location.longitude),
        ).miles
