# Generated by Django 4.2 on 2023-06-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_date_of_publication_photo_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_of_publication',
            field=models.DateField(auto_now=True),
        ),
    ]
