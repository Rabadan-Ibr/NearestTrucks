from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Cargo(models.Model):
    pick_up = models.ForeignKey(
        'locations.Location',
        on_delete=models.CASCADE,
        related_name='pick_up_cargo',
    )
    delivery = models.ForeignKey(
        'locations.Location',
        on_delete=models.CASCADE,
        related_name='delivery_cargo',
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name='Weight',
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
    )
    description = models.TextField(verbose_name='Description', blank=True)
