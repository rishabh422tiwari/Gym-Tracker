# Generated by Django 4.2.4 on 2023-09-14 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_workoutlog_weight'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProgressImage',
        ),
    ]