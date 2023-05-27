from random import randrange

from django.core.management.base import BaseCommand
from rstr import xeger

from locations.models import Location
from trucks.models import Truck
from TrucksSearch import settings


class Command(BaseCommand):
    """
    Fill truck table 20 random trucks, if trucks not exists.
    """
    help = 'Create truck if not exists'

    def handle(self, *args, **options):
        existing_trucks = set(Truck.objects.values_list('id', flat=True))
        existing_zips = Location.objects.all()

        need_count = settings.GENERATE_TRUCK_AMOUNT - len(existing_trucks)
        batch = []
        for _ in range(need_count):
            while True:
                new_id = xeger(settings.TRUCK_ID_REGEX)
                if new_id not in existing_trucks:
                    break

            batch.append(Truck(
                id=new_id,
                location=existing_zips[randrange(0, len(existing_zips))],
                payload=randrange(1, 1000),
            ))

        if len(batch) > 0:
            Truck.objects.bulk_create(batch)
