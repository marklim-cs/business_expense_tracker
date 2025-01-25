# Generated by Django 5.1.5 on 2025-01-25 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provided_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(blank=True, max_length=500, null=True)),
                ('author', models.CharField(max_length=500)),
                ('publisher', models.CharField(max_length=500)),
                ('published_date', models.DateField()),
                ('distribution_expense', models.DecimalField(decimal_places=2, max_digits=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categories')),
            ],
        ),
    ]
