from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('exercises/', views.ExerciseList.as_view()),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view()),
    path('workout/', views.WorkoutListView.as_view()),
    path('workout/<int:pk>/', views.WorkoutDetailView.as_view()),
    path('workout/<int:pk>/exercise/', views.WorkoutExerciseListView.as_view(), name='track-detail'),
    path('workout/<int:pk>/exercise/<int:id>/', views.WorkoutExerciseDetailView.as_view()),
    path('workout/<int:pk>/exercise/start/', views.WorkoutLogListView.as_view()),
    path('workout/<int:pk>/images/', views.ProgressImageListView.as_view()),
    path('workout/<int:pk>/images/<int:id>/', views.ProgressImageDetailView.as_view()),
    path('workout/<int:pk>/exercise/start/<int:id>/', views.WorkoutLogDetailView.as_view()),
    path('workout/history/', views.HistoryAllView.as_view()),
    path('workout/<int:id>/history/', views.HistoryView.as_view()),
    path('profile/', views.UserProfileView)
]