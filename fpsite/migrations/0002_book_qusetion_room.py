# Generated by Django 3.2 on 2022-06-11 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('phone', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qusetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnumber', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnumber', models.CharField(max_length=10)),
                ('detail', models.TextField()),
                ('rent', models.PositiveIntegerField()),
                ('enable', models.BooleanField(default=False)),
            ],
        ),
    ]
