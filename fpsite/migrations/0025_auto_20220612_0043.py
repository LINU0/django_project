# Generated by Django 3.2 on 2022-06-11 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fpsite', '0024_auto_20220611_2322'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account_1',
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
