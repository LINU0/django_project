# Generated by Django 3.2 on 2022-06-11 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0006_alter_account_identity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='image/')),
                ('roomnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpsite.room')),
            ],
        ),
    ]
