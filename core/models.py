from django.db import models

# Create your models here.
class Exercise(models.Model):
    body_part = models.CharField(max_length=255)
    type_of_muscle = models.CharField(max_length=255)
    exercise_name = models.CharField(max_length=255)
    sets = models.CharField(max_length=255)
    reps = models.CharField(max_length=255)

class Workout(models.Model):
    exercises = models.ForeignKey(Exercise, on_delete=)