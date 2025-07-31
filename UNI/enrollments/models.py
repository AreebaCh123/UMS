from django.db import models
from accounts.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

class Withdrawal(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    reason = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} withdrew from {self.course} on {self.date}"
