# Generated by Django 4.2.4 on 2023-08-16 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_part', models.CharField(max_length=255)),
                ('type_of_muscle', models.CharField(max_length=255)),
                ('exercise_name', models.CharField(max_length=255)),
                ('sets', models.CharField(max_length=255)),
                ('reps', models.CharField(max_length=255)),
            ],
        ),
    ]