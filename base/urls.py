from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('exercises/', views.ExerciseList),
    path('exercises/<int:id>/', views.ExerciseDetail),
    path('workout/', views.WorkoutListView),
    path('workout/<int:pk>/', views.WorkoutDetailView),
    path('workout/<int:pk>/exercise/', views.WorkoutExerciseListView, name='track-detail'),
    path('workout/<int:pk>/exercise/<int:id>/', views.WorkoutExerciseDetailView),
    path('workout/<int:pk>/exercise/start/', views.WorkoutLogListView),
    path('workout/<int:pk>/exercise/start/images/', views.ProgressImageView),
    path('workout/<int:pk>/exercise/start/<int:id>/', views.WorkoutLogDetailView),
    path('workout/history/', views.HistoryAllView),
    path('workout/<int:pk>/history/', views.HistoryView)
]