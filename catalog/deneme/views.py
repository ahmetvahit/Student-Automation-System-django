from django.shortcuts import render
from .models import Student
from django.contrib import messages
import sqlite3

# Create your views here.

# Öğrenci Ekleme
def kayit_form(request):
    if request.method=="POST":  
        if request.POST.get('name') and request.POST.get('surname') and request.POST.get('section') and request.POST.get('number'):
            gelen_kayit = Student()
            gelen_kayit.name=request.POST.get('name')
            gelen_kayit.surname = request.POST.get('surname')
            gelen_kayit.section = request.POST.get('section')
            gelen_kayit.number = request.POST.get('number')
            gelen_kayit.save()
            messages.success(request,'Kayıt Başarılı! Hoşgeldiniz '+gelen_kayit.name +' ' + gelen_kayit.surname)
            return render(request, 'addstudent/studentadd.html')
    else:
        return render(request, 'addstudent/studentadd.html')

# Kayıtları Görüntüleme
def displaydata(request):
    results = Student.objects.all()
    return render(request,'addstudent/dataview.html',{"results":results})

# Not Ekleme
def note_adds(request):
    if request.method == "POST":
        if request.POST.get('number') and request.POST.get('midterm_exam') and request.POST.get('final_exam'):
            number = request.POST.get('number')
            kayit = Student.objects.get(number = number)
            kayit.midterm_exam = float(request.POST.get('midterm_exam'))
            kayit.final_exam = float(request.POST.get('final_exam'))
            kayit.exam_average = round(float((kayit.midterm_exam*0.4)+(kayit.final_exam*0.6)),2)

            if (kayit.exam_average >= 90):
                kayit.letter_grade= "AA"
            elif (kayit.exam_average >= 80):
                kayit.letter_grade= "BA"
            elif (kayit.exam_average >= 70):
                kayit.letter_grade= "BB"
            elif (kayit.exam_average >= 60):
                kayit.letter_grade= "CC"
            elif (kayit.exam_average >= 50):
                kayit.letter_grade= "DD"
            else:
                kayit.letter_grade= "FF"
            kayit.save()
            messages.success(request, 'Kayıt Başarılı! Ortalamanız=  ' + str(kayit.exam_average) + kayit.letter_grade)
            return render(request, 'addstudent/addnote.html',{"kayit":kayit})   
    else:
        return render(request, 'addstudent/addnote.html')