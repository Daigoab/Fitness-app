from django.urls import path
from . import views

urlpatterns = [
        path('', views.say_hello, name = 'index'),
        path('update_profile/',views.update_profile, name='update_profile'),
        path('accounts/profile/', views.profile, name='profile'),
        path('workouts/', views.workout_list, name='workout_list'),
        path('workouts/add/', views.add_workout, name='add_workout'),
        path('bmi/', views.bmi, name='bmi'),
]