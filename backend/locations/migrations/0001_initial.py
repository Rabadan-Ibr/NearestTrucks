# Generated by Django 4.2.1 on 2023-05-27 10:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('city', models.CharField(max_length=70, verbose_name='City')),
                ('state', models.CharField(max_length=70, verbose_name='State')),
                ('zip', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{5}$')], verbose_name='Zip Code')),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Latitude')),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Longitude')),
            ],
        ),
    ]
