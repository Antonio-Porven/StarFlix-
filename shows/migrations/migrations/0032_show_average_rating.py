# Generated by Django 4.2.4 on 2023-10-27 21:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0031_alter_showrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='average_rating',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
