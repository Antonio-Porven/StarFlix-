# Generated by Django 4.2.2 on 2023-06-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120, verbose_name='Show Name')),
                ('number_ep', models.CharField(max_length=120, verbose_name='Number of Episodes')),
                ('summary', models.TextField(blank=True, verbose_name='Show Summary')),
                ('Genres', models.CharField(max_length=120, verbose_name='Genre')),
            ],
        ),
    ]
