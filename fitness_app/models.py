from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, default=None)
    profile_photo = CloudinaryField('image', null=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    email=models.EmailField(max_length=100, blank=False, null=False)
    weight=models.IntegerField(default=0, blank=True, null=True)
    height=models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=True)
    exercise_name = models.CharField(max_length=100, blank=True, null=True)
    sets = models.PositiveIntegerField(blank=True, null=True)
    reps = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    cardio_name = models.CharField(max_length=100, blank=True, null=True)
    duration = models.DurationField(default=datetime.timedelta(minutes=0))
    distance = models.FloatField(blank=True, null=True)
    total_calories = models.PositiveIntegerField(blank=True, null=True)
    calories_burned = models.PositiveIntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

class WorkoutComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Bmi(models.Model):
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.bmi

class Challenge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(User, related_name='challenges', blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(User, related_name='programs', blank=True)

    def __str__(self):
        return self.name


class GroupActivity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    participants = models.ManyToManyField(User, related_name='group_activities', blank=True)

    def __str__(self):
        return self.name






