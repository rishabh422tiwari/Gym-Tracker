# Generated by Django 4.2.4 on 2023-09-11 06:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_progressimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ['body_part']},
        ),
        migrations.AlterModelOptions(
            name='workoutlist',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='workoutlog',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='workoutstructure',
            options={'ordering': ['body_part']},
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='rep_count',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='workoutlog',
            name='set_count',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('body_type', models.CharField(choices=[('Ecto', 'Ectomorph'), ('Endo', 'Endomorph'), ('Meso', 'Mesomorph')], default='Meso', max_length=4)),
                ('phone', models.CharField(max_length=255, unique=True)),
                ('birth_date', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
    ]