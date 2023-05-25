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
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Weight')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_cargo', to='locations.location')),
                ('pick_up', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pick_up_cargo', to='locations.location')),
            ],
        ),
    ]