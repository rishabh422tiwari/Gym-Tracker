# Generated by Django 4.2.4 on 2023-08-21 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_workoutlist_workout_struc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutlist',
            name='workout_struc',
        ),
    ]