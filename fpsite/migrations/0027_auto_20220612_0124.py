# Generated by Django 3.2 on 2022-06-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0026_auto_20220612_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
    ]
