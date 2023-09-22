from rest_framework import serializers
from django.db.models import Avg, Count, Sum
from .models import Exercise, WorkoutList, WorkoutStructure, WorkoutLog, UserProfile, ProgressImage, UserProfile

class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['height', 'weight', 'body_type', 'phone', 'birth_date', 'user']

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'body_part', 'muscle_name', 'exercise_name', 'sets', 'reps']

class WorkoutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutStructure
        fields = ['id', 'body_part', 'muscle_name', 'exercise_name', 'sets', 'reps', 'workout']

class WorkoutListSerializer(serializers.ModelSerializer):

    # workout_lists = WorkoutCreateSerializer(many=True,
    #                                         read_only=True)
    class Meta:
        model = WorkoutList
        fields = ['id','title', 'created_at']

class ProgressImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressImage
        fields = ['id', 'workout_no','created_at', 'image']

class WorkoutLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutLog
        fields = ['id', 'work_list','work_structure', 'created_at', 'set_count', 'rep_count', 'weight', 'note']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'height', 'weight', 'body_type', 'phone', 'birth_date']
