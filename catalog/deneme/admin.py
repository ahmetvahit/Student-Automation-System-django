from django.contrib import admin
from django.contrib.admin import register
# Register your models here.
from .models import Student

admin.site.register(Student)