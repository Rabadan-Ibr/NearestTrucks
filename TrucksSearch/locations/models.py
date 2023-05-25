from django.db import models

from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


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
