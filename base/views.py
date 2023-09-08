from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ExerciseSerializer, WorkoutListSerializer, WorkoutCreateSerializer, WorkoutLogSerializer \
                        , ProgressImageSerializer
from .models import Exercise, WorkoutList , WorkoutStructure, WorkoutLog, ProgressImage
from datetime import date

@api_view(['GET', 'POST'])
def ExerciseList(request):
    exercise = Exercise.objects.all()
    if request.method == 'GET':
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExerciseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ExerciseDetail(request, id):
    exercise = Exercise.objects.get(id=id)
    if request.method == 'GET':
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ExerciseSerializer(exercise, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def WorkoutListView(request):
    workout = WorkoutList.objects.all()
    if request.method == 'GET':
        serializer = WorkoutListSerializer(workout, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
#  context={'request': request}

@api_view(['GET','PUT', 'DELETE'])
def WorkoutDetailView(request, pk):
    workout = WorkoutList.objects.get(id=pk)
    if request.method == 'GET':
        serializer = WorkoutListSerializer(workout)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkoutListSerializer(workout, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def WorkoutExerciseListView(request, pk):
    custom_workout = WorkoutStructure.objects.filter(workout=pk)
    if request.method == 'GET':
        serializer = WorkoutCreateSerializer(custom_workout, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def WorkoutExerciseDetailView(request, pk, id):
    exercise_no = WorkoutStructure.objects.get(id=id)
    if request.method == 'GET':
        serializer = WorkoutCreateSerializer(exercise_no)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkoutCreateSerializer(exercise_no, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        exercise_no.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def WorkoutLogListView(request, pk):
    log = WorkoutLog.objects.filter(work_list = pk, created_at= date.today())
    if request.method == 'GET':
        serializer = WorkoutLogSerializer(log, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutLogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def WorkoutLogDetailView(request, pk, id):
    log = WorkoutLog.objects.get(work_list = pk, id=id)
    if request.method == 'GET':
        serializer = WorkoutLogSerializer(log, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkoutLogSerializer(log, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def ProgressImageView(request, pk):
    queryset = ProgressImage.objects.filter(workout_log__work_list = pk, workout_log__created_at=date.today())
    if request.method == 'GET':
        serializer = ProgressImageSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProgressImageSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

@api_view()
def HistoryAllView(request):
    queryset = WorkoutLog.objects.select_related('ProgressImage').all()
    serializer = WorkoutLogSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def HistoryView(requestm, pk):
    queryset = WorkoutLog.objects.filter(work_list=pk)
    serializer = WorkoutLogSerializer(queryset, many=True)
    return Response(serializer.data)
