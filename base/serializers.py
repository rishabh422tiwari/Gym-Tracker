from rest_framework import serializers
from django.db.models import Avg, Count, Sum
from .models import Exercise, WorkoutList, WorkoutStructure

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps']

class WorkoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutStructure
        fields = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps', 'workout_no']

class WorkoutListSerializer(serializers.ModelSerializer):
    workout_lists = WorkoutCreateSerializer(read_only=True,
                                            many=True)

    class Meta:
        model = WorkoutList
        fields = ['title', 'created_at', 'workout_lists']
