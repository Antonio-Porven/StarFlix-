# Generated by Django 4.2.4 on 2023-10-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0019_alter_profile_bio_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Profile_Image',
            field=models.ImageField(blank=True, default='ProfileImage.png', max_length=2000, null=True, upload_to='images/', verbose_name='Profile Picture'),
        ),
    ]
