from random import randrange

from config.celery import app
from locations.models import Location
from trucks.models import Truck


@app.task()
def update_locations():
    """
    Updates all trucks' csv
    """
    trucks = Truck.objects.all()
    existing_zips = Location.objects.all()

    for truck in trucks:
        loc_pos = randrange(0, len(existing_zips))
        truck.location = existing_zips[loc_pos]

    Truck.objects.bulk_update(trucks, ['location'], batch_size=50)
