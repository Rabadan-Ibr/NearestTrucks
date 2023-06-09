# Generated by Django 4.2.1 on 2023-05-27 10:42

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[1-9]{1}[0-9]{3}[A-Z]{1}$')], verbose_name='ID')),
                ('payload', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Payload')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck_location', to='locations.location')),
            ],
        ),
    ]
