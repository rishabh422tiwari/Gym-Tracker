from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from .serializers import ExerciseSerializer, WorkoutListSerializer, WorkoutCreateSerializer, WorkoutLogSerializer \
                            , ProgressImageSerializer, UserProfileSerializer

from .models import Exercise, WorkoutList , WorkoutStructure, WorkoutLog, ProgressImage, UserProfile
from datetime import date

class ExerciseList(ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request:)
    #     exercise = Exercise.objects.all()
    #     serializer = ExerciseSerializer(exercise, many=True)
        # return Response(serializer.data)

    # def post(self, request):
    #     serializer = ExerciseSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class ExerciseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

    # def get(self, request, id):
    #     exercise = Exercise.objects.get(id=id)
    #     serializer = ExerciseSerializer(exercise)
    #     return Response(serializer.data)
    # def put(self, request, id):
    #     exercise = Exercise.objects.get(id=id)
    #     serializer = ExerciseSerializer(exercise, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    # def delete(self, request, id):
    #     exercise = Exercise.objects.get(id=id)
    #     exercise.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class WorkoutListView(ListCreateAPIView):
    queryset = WorkoutList.objects.all()
    serializer_class = WorkoutListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    
    # def get(self, request):
    #     workout = WorkoutList.objects.all()
    #     serializer = WorkoutListSerializer(workout, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = WorkoutListSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

class WorkoutDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkoutList.objects.all()
    serializer_class =  WorkoutListSerializer
    # lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    # def get(self, request, pk):
    #     workout = WorkoutList.objects.get(id=pk)
    #     serializer = WorkoutListSerializer(workout)
    #     return Response(serializer.data)
    # def put(self, request, pk):
    #     workout = WorkoutList.objects.get(id=pk)
    #     serializer = WorkoutListSerializer(workout, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    # def delete(self, request, pk):
    #     workout = WorkoutList.objects.get(id=pk)
    #     workout.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class WorkoutExerciseListView(ListCreateAPIView):
    queryset = WorkoutStructure.objects.all()
    serializer_class = WorkoutCreateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # def get(self, request, pk):
    #     custom_workout = WorkoutStructure.objects.filter(workout=pk)
    #     serializer = WorkoutCreateSerializer(custom_workout, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request, pk):
    #     serializer = WorkoutCreateSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class WorkoutExerciseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkoutStructure.objects.all()
    serializer_class = WorkoutCreateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get(self, request, pk, id):
    #     exercise_no = WorkoutStructure.objects.get(id=id)
    #     serializer = WorkoutCreateSerializer(exercise_no)
    #     return Response(serializer.data)

    # def put(self, request, pk, id):
    #     exercise_no = WorkoutStructure.objects.get(id=id)
    #     serializer = WorkoutCreateSerializer(exercise_no, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    
    # def delete(self, request, pk, id):
    #     exercise_no = WorkoutStructure.objects.get(id=id)
    #     exercise_no.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class WorkoutLogListView(ListCreateAPIView):

    def get_queryset(self):
        return WorkoutLog.objects.filter(work_list = self.kwargs['pk'], created_at= date.today())
    
    serializer_class = WorkoutLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # def get(self, request, pk):
    #     log = WorkoutLog.objects.filter(work_list = pk, created_at= date.today())
    #     serializer = WorkoutLogSerializer(log, many=True, context={'request': request})
    #     return Response(serializer.data)
    
    # def post(self, request, pk):
    #     serializer = WorkoutLogSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class WorkoutLogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkoutLog.objects.all()
    serializer_class = WorkoutLogSerializer
    lookup_field = 'id'


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


    # def get(self, request, pk, id):
    #     log = WorkoutLog.objects.get(work_list = pk, id=id)
    #     serializer = WorkoutLogSerializer(log, context={'request': request})
    #     return Response(serializer.data)
    # def put(self, request, pk, id):
    #     log = WorkoutLog.objects.get(work_list = pk, id=id)
    #     serializer = WorkoutLogSerializer(log, data=request.data) 
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # def delete(self, request, pk, id):
    #     log = WorkoutLog.objects.get(work_list = pk, id=id)
    #     log.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProgressImageListView(ListCreateAPIView):
    serializer_class = ProgressImageSerializer
    
    def get_queryset(self):
        return ProgressImage.objects.filter(workout_no=self.kwargs['pk'])
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request, pk):
    #     queryset = ProgressImage.objects.filter(workout_no__id = pk)
    #     serializer = ProgressImageSerializer(queryset, many=True)
    #     return Response(serializer.data)
    # def post(self, request, pk):
    #     queryset = ProgressImage.objects.filter(workout_no__id = pk)
    #     serializer = ProgressImageSerializer(queryset, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

class ProgressImageDetailView(ListAPIView):
    serializer_class = ProgressImageSerializer

    def get_queryset(self):
        return ProgressImage.objects.filter(id=self.kwargs['id'])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class HistoryAllView(ListAPIView):
    queryset = WorkoutLog.objects.all()
    serializer_class = WorkoutLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self, request):
    #     queryset = WorkoutLog.objects.all()
    #     serializer = WorkoutLogSerializer(queryset, many=True)
    #     return Response(serializer.data)

class HistoryView(ListAPIView):
    def get_queryset(self):
        return WorkoutLog.objects.filter(work_list=self.kwargs['id'])

    serializer_class = WorkoutLogSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def get(self, request, pk):
    #     queryset = WorkoutLog.objects.filter(work_list=pk)
    #     serializer = WorkoutLogSerializer(queryset, many=True)
    #     return Response(serializer.data)

class UserProfileView(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer





































# @api_view(['GET', 'POST'])
# def ExerciseList(request):
#     exercise = Exercise.objects.all()
#     if request.method == 'GET':
#         serializer = ExerciseSerializer(exercise, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ExerciseSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def ExerciseDetail(request, id):
#     exercise = Exercise.objects.get(id=id)
#     if request.method == 'GET':
#         serializer = ExerciseSerializer(exercise)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ExerciseSerializer(exercise, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         exercise.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def WorkoutListView(request):
#     workout = WorkoutList.objects.all()
#     if request.method == 'GET':
#         serializer = WorkoutListSerializer(workout, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WorkoutListSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#  context={'request': request}

# @api_view(['GET','PUT', 'DELETE'])
# def WorkoutDetailView(request, pk):
#     workout = WorkoutList.objects.get(id=pk)
#     if request.method == 'GET':
#         serializer = WorkoutListSerializer(workout)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = WorkoutListSerializer(workout, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         workout.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def WorkoutExerciseListView(request, pk):
#     custom_workout = WorkoutStructure.objects.filter(workout=pk)
#     if request.method == 'GET':
#         serializer = WorkoutCreateSerializer(custom_workout, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WorkoutCreateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT', 'DELETE'])
# def WorkoutExerciseDetailView(request, pk, id):
#     exercise_no = WorkoutStructure.objects.get(id=id)
#     if request.method == 'GET':
#         serializer = WorkoutCreateSerializer(exercise_no)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = WorkoutCreateSerializer(exercise_no, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         exercise_no.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# @api_view(['GET', 'POST'])
# def WorkoutLogListView(request, pk):
#     log = WorkoutLog.objects.filter(work_list = pk, created_at= date.today())
#     if request.method == 'GET':
#         serializer = WorkoutLogSerializer(log, many=True, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = WorkoutLogSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['GET', 'PUT', 'DELETE'])
# def WorkoutLogDetailView(request, pk, id):
#     log = WorkoutLog.objects.get(work_list = pk, id=id)
#     if request.method == 'GET':
#         serializer = WorkoutLogSerializer(log, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = WorkoutLogSerializer(log, data=request.data) 
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         log.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def ProgressImageView(request, pk):
#     queryset = ProgressImage.objects.filter(workout_log__work_list = pk, workout_log__created_at=date.today())
#     if request.method == 'GET':
#         serializer = ProgressImageSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProgressImageSerializer(queryset, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()


# @api_view()
# def HistoryAllView(request):
#     queryset = WorkoutLog.objects.select_related('ProgressImage').all()
#     serializer = WorkoutLogSerializer(queryset, many=True)
#     return Response(serializer.data)

# @api_view()
# def HistoryView(request, pk):
#     queryset = WorkoutLog.objects.filter(work_list=pk)
#     serializer = WorkoutLogSerializer(queryset, many=True)
#     return Response(serializer.data)
