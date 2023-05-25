from random import randrange

from django.core.management.base import BaseCommand

from locations.models import Location
from trucks.models import Truck

from rstr import xeger


class Command(BaseCommand):
    help = 'Create truck if not exists'

    def handle(self, *args, **options):
        existing_trucks = set(Truck.objects.values_list('id', flat=True))
        existing_zips = Location.objects.values_list('zip', flat=True)
        need_count = 20 - len(existing_trucks)
        batch = []
        for i in range(need_count):
            while True:
                id = xeger(r'^[0-9]{4}[A-Z]{1}$')
                if id not in existing_trucks:
                    break
            loc_pos = randrange(0, len(existing_zips))
            location = Location.objects.get(zip=existing_zips[loc_pos])
            payload = randrange(1, 1000)
            batch.append(Truck(id=id, location=location, payload=payload))
        if len(batch) > 0:
            Truck.objects.bulk_create(batch)
