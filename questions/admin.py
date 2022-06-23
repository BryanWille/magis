from django.contrib import admin

# Register your models here.
from .models import *

from . import models

class TeacherAdminArea(admin.AdminSite):
    site_header = "Teacher Database"

class StudentAdminArea(admin.AdminSite):
    site_header = "Student Database"

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ScoreBoard)

teacher_site = TeacherAdminArea(name='TeacherAdmin')
teacher_site.register(Course)
teacher_site.register(Question, QuestionAdmin)
teacher_site.register(Answer)

student_site = StudentAdminArea(name='StudentAdmin')
student_site.register(Question, QuestionAdmin)



