# Generated by Django 4.2.4 on 2023-10-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0022_alter_movie_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='Cover_Image',
            field=models.ImageField(max_length=2000, null=True, upload_to='ShowCovers/'),
        ),
    ]
