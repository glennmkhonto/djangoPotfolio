# Generated by Django 4.0.3 on 2022-10-18 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='country',
        ),
    ]
