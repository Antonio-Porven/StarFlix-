# Generated by Django 4.2.2 on 2023-06-25 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shows',
            new_name='Show',
        ),
    ]