# Generated by Django 4.2.2 on 2023-06-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_remove_show_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='Cover_Image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
