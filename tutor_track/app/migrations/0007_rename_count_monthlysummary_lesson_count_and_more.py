# Generated by Django 5.1.4 on 2025-02-08 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_monthlysummary_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthlysummary',
            old_name='count',
            new_name='lesson_count',
        ),
        migrations.RenameField(
            model_name='monthlysummary',
            old_name='lesson',
            new_name='student_card',
        ),
        migrations.RemoveField(
            model_name='monthlysummary',
            name='total_money',
        ),
    ]
