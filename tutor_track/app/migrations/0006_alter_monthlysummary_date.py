# Generated by Django 5.1.4 on 2025-02-07 18:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_day_name_monthlysummary_delete_monthlyrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlysummary',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
