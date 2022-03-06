from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from . import views

urlpatterns = [
    path('student_form', views.kayit_form, name='student_form'),
    path('dataview', views.displaydata, name='dataview'),
    path('noteadd', views.note_adds,name='noteadd'),
    
]