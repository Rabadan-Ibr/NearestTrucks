import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-udm3$6u2*_1tb$nf_aru^m2(o3pph&(m-a*-ah)f!vmpgaym&&'
)

DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = []

STATIC_URL = 'static/'

CSV_DIR = BASE_DIR / 'data' / 'csv'

LOCATION_CSV_PATH = CSV_DIR / 'locations.csv'

DEFAULT_MAX_DISTANCE = 450

GENERATE_TRUCK_AMOUNT = 20
