from rest_framework import serializers
from .models import Exercise, WorkoutList, WorkoutStructure

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps']
    
class WorkoutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutList
        fields = ['id_no','title','created_at']

class WorkoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutStructure
        fields = ['body_part', 'muscle_name', 'exercise_name', 'sets', 'reps']