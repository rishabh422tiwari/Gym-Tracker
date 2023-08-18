from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('exercises/', views.exercise_list),
    path('exercises/workout/', views.workout_list),
    path('exercises/workout/<id>/', views.workout_create)
]