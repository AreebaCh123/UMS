from django.contrib import admin
from .models import Course, Timetable

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'teacher']
   

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'day', 'start_time', 'end_time']
   