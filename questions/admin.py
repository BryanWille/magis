from tokenize import group
from django.contrib import admin

# Register your models here.
from .models import *

# class TeacherAdminArea(admin.AdminSite):
#     site_header = "Teacher Database"

# class StudentAdminArea(admin.AdminSite):
#     site_header = "Student Database"

class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]

# class TeacherAdminPermissions(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#     def has_add_permission(self, request):
#         return True
#     def has_change_permission(self, request, obj=None):
#         return True
#     def has_delete_permission(self, request, obj=None):
#         return True
#     def has_view_permission(self, request, obj=None):
#         return True

# class StudentAdminPermissions(admin.ModelAdmin):
#     inlines = [AnswerAdmin]
#     def has_add_permission(self, request):
#         return True
#     def has_change_permission(self, request, obj=None):
#         return False
#     def has_delete_permission(self, request, obj=None):
#         return False
#     def has_view_permission(self, request, obj=None):
#         return True

admin.site.register(Course)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(ScoreBoard)

# teacher_site = TeacherAdminArea(name='TeacherAdmin')
# teacher_site.register(Course)
# teacher_site.register(Question, TeacherAdminPermissions)

# student_site = StudentAdminArea(name='StudentAdmin')
# student_site.register(Question, StudentAdminPermissions)





