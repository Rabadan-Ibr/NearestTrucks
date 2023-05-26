import csv
import logging

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from locations.models import Location
from TrucksSearch import settings


class Command(BaseCommand):
    """
    Fill csv table with data from .csv
    """
    help = 'Load locations from .csv'

    def handle(self, *args, **kwargs):
        logger = logging.getLogger(__name__)
        path = settings.LOCATION_CSV_PATH
        try:
            with open(path, newline='', encoding='utf-8') as file:
                csvfile = csv.DictReader(file)
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

                    if len(batch) == 200:
                        Location.objects.bulk_create(batch)
                        batch = []
                if len(batch) > 0:
                    Location.objects.bulk_create(batch)

        except FileNotFoundError:
            logger.error(f'Error: .csv file in path "{path}" not found.')
        except KeyError:
            logger.error('Error: .csv file is not correct format.')
        except ValidationError:
            logger.error('Error: in .csv file some data is incorrect.')
