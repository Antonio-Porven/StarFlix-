# Generated by Django 4.2.4 on 2023-10-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0028_alter_showrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showrating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
