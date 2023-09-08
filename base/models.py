from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Exercise(models.Model):
    body_part = models.CharField(max_length=255)
    muscle_name = models.CharField(max_length=255)
    exercise_name = models.CharField(max_length=255)
    sets = models.CharField(max_length=255)
    reps = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.exercise_name
    
    class Meta:
        ordering = ['body_part']

class WorkoutList(models.Model):  
    created_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, default="")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


    
class WorkoutStructure(models.Model):
    workout = models.ForeignKey(WorkoutList, on_delete=models.CASCADE, related_name='workout_lists')
    body_part = models.CharField(max_length=255,default="", blank=True)
    muscle_name = models.CharField(max_length=255,default="", blank=True)
    exercise_name = models.CharField(max_length=255, default="", blank=True)
    sets = models.CharField(max_length=255, default="", blank=True)
    reps = models.CharField(max_length=255, default="", blank=True)

    def __str__(self) -> str:
        return self.exercise_name
    
    class Meta:
        ordering = ['body_part']    

class WorkoutLog(models.Model):
    created_at = models.DateField(auto_now_add=True)
    work_list = models.ForeignKey(WorkoutList, on_delete=models.CASCADE)
    work_structure = models.ForeignKey(WorkoutStructure, on_delete=models.CASCADE)
    set_count = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    rep_count = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(50)]
    )
    note = models.TextField()

    def __str__(self) -> str:
        return self.note

    class Meta:
        ordering = ['created_at']

class ProgressImage(models.Model):
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='base/images', null=True)
