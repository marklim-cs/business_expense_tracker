# Generated by Django 5.1.5 on 2025-01-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
