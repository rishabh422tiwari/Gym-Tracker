from django.contrib import admin
from .models import Exercise

# Register your models here.
@admin.register(Exercise)
class ExerciseModel(admin.ModelAdmin):
    pass