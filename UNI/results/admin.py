from django.contrib import admin
from .models import Result, Attendance

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'grade']
    

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'date', 'status']
