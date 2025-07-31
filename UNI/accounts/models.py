from django.db import models
from django.contrib.auth.models import AbstractUser
from departments.models import Department

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'student'),
        ('faculty', 'faculty'),
        ('admin', 'admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.user_type})"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.department}"

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
