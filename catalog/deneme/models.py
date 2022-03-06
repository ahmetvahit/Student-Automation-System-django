from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Öğrenci Ad')
    surname = models.CharField(max_length=100, verbose_name='Öğrenci Soyad')
    section = models.TextField(verbose_name='Bölüm')
    number = models.CharField(max_length=50, verbose_name='TC Kimlik No')
    midterm_exam = models.FloatField(verbose_name='Vize Notu',null=True)
    final_exam = models.FloatField(verbose_name='Final Notu',null=True)
    exam_average = models.FloatField( verbose_name='Ortalama Not',null=True)
    letter_grade = models.CharField(max_length=50, verbose_name='Harf Notu',null=True)

    def __str__(self):
        return "%s"%(self.number)
