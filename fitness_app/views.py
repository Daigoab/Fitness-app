from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import *
from .models import Workout, WorkoutComment
from django.views.generic import DetailView
from django.db import IntegrityError
from django.http import HttpResponse

def say_hello(request):
    context = {'message': 'Hello Daigo'}
    return render(request, 'index.html', context)

@login_required(login_url="/accounts/login/")
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "profile.html", {"profile": profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    profile = request.user.profile  # Retrieve the profile of the logged-in user
    form = UpdateProfileForm(instance=profile)

    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')

    return render(request, 'update_profile.html', {"form": form})



@login_required(login_url="/accounts/login/")
@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    
    return render(request, 'add_workout.html', {'form': form})

def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workout_list.html', {'workouts': workouts})

def bmi(request):
    context = {}
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")

        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial"))/2.205
            height = (float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100

        bmi = (weight/(height**2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(weight=weight, height=height, bmi=round(bmi))
        if bmi < 16:
            state = "Severely underweight"
        elif bmi > 16 and bmi < 17:
            state = "Moderately underweight"
        elif bmi > 17 and bmi < 18:
            state = "Mildly underweight"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Slightly obese"
        elif bmi > 35 and bmi < 40:
            state = "Moderately Obese"
        elif bmi > 40:
            state = "Severe obesity, seek medical attention"

        context["bmi"] = round(bmi)
        context["state"] = state



    return render(request, "bmi.html", context)
