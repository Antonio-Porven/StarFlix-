# Generated by Django 4.2.2 on 2023-08-19 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0018_profile_backgroundcolor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Bio',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=120000, verbose_name='Bio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='Profile_Image',
            field=models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/', verbose_name='Profile Picture'),
        ),
    ]