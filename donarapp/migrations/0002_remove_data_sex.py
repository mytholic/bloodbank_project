# Generated by Django 3.2.4 on 2021-06-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donarapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='sex',
        ),
    ]
