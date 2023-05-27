from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from config import settings


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

    class Meta:
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'
        ordering = ('id',)

    def __str__(self):
        return f'ID:{self.id}, max_load:{self.payload}'
