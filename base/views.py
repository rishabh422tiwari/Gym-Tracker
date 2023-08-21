from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ExerciseSerializer, WorkoutListSerializer, WorkoutCreateSerializer
from .models import Exercise, WorkoutList , WorkoutStructure

@api_view()
def ExerciseList(request):
    exercise = Exercise.objects.all()
    serializer = ExerciseSerializer(exercise, many=True)
    return Response(serializer.data)

@api_view()
def WorkoutListView(request):
    workout = WorkoutList.objects.all()
    serializer = WorkoutListSerializer(workout, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET','POST','PUT','DELETE'])
def WorkoutDetailView(request, pk):
    custom_workout = WorkoutStructure.objects.filter(workout_no=pk)

    if request.method == 'GET':
        serializer = WorkoutCreateSerializer(custom_workout, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        serializer = WorkoutCreateSerializer(custom_workout,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        custom_workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
























 


# class ExerciseList(APIView):
#     def get(self, request):
#         exercise = Exercise.objects.all()
#         serializer = ExerciseSerializer(exercise, many=True)
#         return Response(serializer.data)

# class WorkoutListView(APIView):
#     def get(self, request):
#         workout = WorkoutList.objects.all()
#         serializer = WorkoutListSerializer(workout, many=True, context={'request': request})
#         return Response(serializer.data)

# class WorkoutDetailView(APIView):
#     def get(self, request, id):
#         custom_workout = WorkoutStructure.objects.filter(workout_id=id) 
#         serializer = WorkoutCreateSerializer(custom_workout, many=True)
#         return Response(serializer.data)
#     def post(self, request, id):
#         serializer = WorkoutCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         serializer.validated_data
#         return Response('ok')
 