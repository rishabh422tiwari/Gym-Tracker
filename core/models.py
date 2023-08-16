from django.db import models

# Create your models here.
class Exercise(models.Model):
    body_part = models.CharField(max_length=255)
    muscle_name = models.CharField(max_length=255)
    exercise_name = models.CharField(max_length=255)
    sets = models.CharField(max_length=255)
    reps = models.CharField(max_length=255)

class Workouts(models.Model):
    id_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    created_at = models.DateField(auto_now_add=True)

class Workoutplan(models.Model):
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE)
    body_part = models.CharField(max_length=255,default="", blank=True)
    muscle_name = models.CharField(max_length=255,default="", blank=True)
    exercise_name = models.CharField(max_length=255, default="", blank=True)
    sets = models.CharField(max_length=255, default="", blank=True)
    reps = models.CharField(max_length=255, default="", blank=True)