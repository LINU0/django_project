# Generated by Django 3.2 on 2022-06-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0017_alter_account_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='identity',
            field=models.CharField(choices=[('landlord', '房東'), ('resident', '住戶'), ('non-resident', '非住戶')], default='房東', max_length=20),
        ),
    ]
