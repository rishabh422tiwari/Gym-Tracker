from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExerciseSerializer, WorkoutListSerializer, WorkoutCreateSerializer
from .models import Exercise, WorkoutList, WorkoutStructure


@api_view()
def exercise_list(request):
    exercise = Exercise.objects.all()
    serializer = ExerciseSerializer(exercise, many=True)
    return Response(serializer.data)

@api_view()
def workout_list(request):
    workout = WorkoutList.objects.all()
    serializer = WorkoutListSerializer(workout, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def workout_create(request, id):
    custom_workout = WorkoutStructure.objects.filter(workout_id=id)
    serializer = WorkoutCreateSerializer(custom_workout, many=True)
    return Response(serializer.data)

