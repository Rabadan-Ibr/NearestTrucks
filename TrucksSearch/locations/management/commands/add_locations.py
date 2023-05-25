import csv

from django.core.management.base import BaseCommand

from TrucksSearch import settings
from locations.models import Location


class Command(BaseCommand):
    help = 'Load locations from .csv'

    def handle(self, *args, **kwargs):
        path = f'{settings.BASE_DIR}/data/locations/uszips.csv'
        try:
            with open(path, newline='', encoding='utf-8') as file:
                csvfile = csv.DictReader(file, delimiter=',')
                existing_zips = set(
                    Location.objects.values_list('zip', flat=True)
                )
                batch = []
                for row in csvfile:
                    if row['zip'] in existing_zips:
                        continue
                    batch.append(Location(
                        zip=row['zip'],
                        city=row['city'],
                        state=row['state_name'],
                        latitude=row['lat'],
                        longitude=row['lng'],
                    ))
                    if len(batch) == 100:
                        Location.objects.bulk_create(batch)
                        batch = []
        except Exception as err:
            print(f'Ошибка: {str(err)}')
