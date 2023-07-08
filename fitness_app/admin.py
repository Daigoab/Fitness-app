from django.contrib import admin
from .models import Challenge, Program, GroupActivity

# Register your models here.
admin.site.register(Challenge)
admin.site.register(Program)
admin.site.register(GroupActivity)