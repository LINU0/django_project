# Generated by Django 3.2 on 2022-06-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0021_alter_account_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='identity',
            field=models.CharField(choices=[('resident', '住戶'), ('non-resident', '非住戶'), ('landlord', '房東')], default='住戶', max_length=20),
        ),
    ]
