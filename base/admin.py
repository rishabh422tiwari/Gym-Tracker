from collections import Counter
from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.http.request import HttpRequest
from . import models
from django.db.models import Count

@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps']
    list_filter = ['body_part']
    list_per_page = 10
    search_fields = ['body_part__istartswith','exercise_name__istartswith']

class WorkoutStructureInline(admin.StackedInline):
    model = models.WorkoutStructure
    min_num = 1
    max_num = 10
    extra = 0

@admin.register(models.WorkoutList)
class WorkoutListAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'title', 'exercise_count']
    list_per_page = 5
    inlines = [WorkoutStructureInline]
    search_fields = ['title']

    @admin.display(ordering='exercise_count')
    def exercise_count(self, exercise):
        url = reverse('admin:base_workoutstructure_changelist')
        return format_html('<a href="{}">{}<a>', url,  exercise.exercise_count)
        
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            exercise_count=Count('workout_lists')
        )

@admin.register(models.WorkoutStructure)
class WorkoutStructureAdmin(admin.ModelAdmin):
    list_display = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps', 'workout_title']
    list_per_page = 10
    list_select_related = ['workout']
    search_fields = ['exercise_name']

    def workout_title(self, workoutstructure):
        return workoutstructure.workout.title

@admin.register(models.WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    autocomplete_fields = ['work_list', 'work_structure']
    list_display = ['created_at', 'work_list', 'work_structure', 'set_count', 'rep_count', 'note']
    list_editable = ['set_count', 'rep_count']
    list_filter = ['created_at']
    list_per_page = 10