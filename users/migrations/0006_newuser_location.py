# Generated by Django 4.1.2 on 2022-10-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_newuser_city_newuser_photo_alter_newuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
