from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('exercises/', views.ExerciseList),
    path('workout/', views.WorkoutListView,),
    path('workout/<int:pk>/', views.WorkoutDetailView,  name='get-workout-detail')
]