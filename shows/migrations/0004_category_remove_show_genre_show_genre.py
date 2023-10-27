# Generated by Django 4.2.2 on 2023-06-26 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_rename_genres_show_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=120, verbose_name='Genres')),
            ],
        ),
        migrations.RemoveField(
            model_name='show',
            name='Genre',
        ),
        migrations.AddField(
            model_name='show',
            name='Genre',
            field=models.ManyToManyField(to='shows.category'),
        ),
    ]
