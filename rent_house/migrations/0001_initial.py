# Generated by Django 5.0.4 on 2024-05-06 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
        ('users', '0004_usermodel_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField()),
                ('neighborhood', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('policy', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.country')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermodel')),
            ],
        ),
    ]