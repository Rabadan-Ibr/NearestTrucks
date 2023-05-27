from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from TrucksSearch import settings


class Truck(models.Model):
    id = models.CharField(
        verbose_name='ID',
        validators=[RegexValidator(settings.TRUCK_ID_REGEX)],
        max_length=5,
        primary_key=True,
    )
    location = models.ForeignKey(
        'locations.Location',
        on_delete=models.CASCADE,
        related_name='truck_location',
    )
    payload = models.PositiveIntegerField(
        verbose_name='Payload',
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
    )
