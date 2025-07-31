from django.db import models
from accounts.models import Teacher

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Timetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course} - {self.day} ({self.start_time} to {self.end_time})"
