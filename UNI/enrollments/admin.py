from django.contrib import admin
from .models import Enrollment, Withdrawal

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'enrolled_on']
   

@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'reason', 'date']
 