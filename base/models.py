from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    body_lean = 'Ecto'
    body_healthy = 'Endo'
    body_normal = 'Meso'

    body_type_choices = [
        (body_lean, 'Ectomorph'),
        (body_healthy, 'Endomorph'),
        (body_normal, 'Mesomorph'),
    ]

    height = models.CharField(max_length=255)
    weight = models.IntegerField()
    body_type = models.CharField(max_length=4, choices=body_type_choices, default=body_normal)
    phone = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField(null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']
        

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
    weight = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(300)]
    )
    note = models.TextField()

    def __str__(self) -> str:
        return self.note

    class Meta:
        ordering = ['created_at']

class ProgressImage(models.Model):
    workout_no = models.ForeignKey(WorkoutList, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='base/images', null=True)
