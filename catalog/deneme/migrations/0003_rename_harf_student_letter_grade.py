# Generated by Django 4.0.1 on 2022-01-20 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deneme', '0002_student_harf_alter_student_exam_average_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='harf',
            new_name='letter_grade',
        ),
    ]