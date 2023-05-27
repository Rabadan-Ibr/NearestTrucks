from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from trucks.models import Truck


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

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return f'{self.id}: {self.pick_up} -> {self.delivery}'

    @property
    def trucks(self):
        """
        Return: list of dicts with truck id and distance to pick up cargo.
        Example: [{'truck_id': 1111A, 'distance': 100}, ...]
        """
        trucks = Truck.objects.select_related('location')
        return [{
            'truck_id': truck.id,
            'distance': truck.location.get_distance(self.pick_up),
        } for truck in trucks]
