from django import forms
from django.forms import ModelForm
from .models import *


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'first_name', 'last_name', 'city', 'email', 'weight', 'height')

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('title', 'exercise_name', 'sets', 'reps', 'weight', 'cardio_name', 'duration', 'distance', 'total_calories', 'calories_burned' )

class WorkoutCommentForm (forms.ModelForm):
    class Meta:
        model = WorkoutComment
        fields = ('comment',)        
