# Generated by Django 3.2 on 2022-06-11 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpsite', '0008_alter_question_roomnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=20)),
                ('date_start', models.DateField(null=True)),
                ('date_end', models.DateField(null=True)),
                ('emergencycontact', models.CharField(max_length=20)),
                ('emergencynumber', models.CharField(max_length=20)),
                ('enable', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpsite.account')),
            ],
        ),
    ]
