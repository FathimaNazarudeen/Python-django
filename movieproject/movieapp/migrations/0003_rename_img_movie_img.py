# Generated by Django 4.2.5 on 2023-09-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Img',
            new_name='img',
        ),
    ]
