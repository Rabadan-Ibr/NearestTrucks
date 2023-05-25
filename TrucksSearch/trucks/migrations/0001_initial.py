# Generated by Django 4.2.1 on 2023-05-25 14:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9]{4}[A-Z]{1}$')], verbose_name='ID')),
                ('payload', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Payload')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck_location', to='locations.location')),
            ],
        ),
    ]
