# Generated by Django 3.2 on 2022-06-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0013_alter_book_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='date_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resident',
            name='date_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]