from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from .models import *
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Course.objects.filter(teacher__user=user)
        elif user.user_type == 'student':
            return Course.objects.filter(enrollment__student__user=user).distinct()
        return Course.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'student':
            return Student.objects.filter(user=user)
        elif user.user_type == 'faculty':
            return Student.objects.filter(enrollment__course__teacher__user=user).distinct()
        return Student.objects.all()

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Teacher.objects.filter(department=user.teacher.department)
        elif user.user_type == 'student':
            return Teacher.objects.filter(department=user.student.department)
        return Teacher.objects.all()

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Enrollment.objects.filter(course__teacher__user=user)
        elif user.user_type == 'student':
            return Enrollment.objects.filter(student__user=user)
        return Enrollment.objects.all()

class WithdrawalViewSet(viewsets.ModelViewSet):
    queryset = Withdrawal.objects.all()
    serializer_class = WithdrawalSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Withdrawal.objects.filter(course__teacher__user=user)
        elif user.user_type == 'student':
            return Withdrawal.objects.filter(student__user=user)
        return Withdrawal.objects.all()

class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Result.objects.filter(course__teacher__user=user)
        elif user.user_type == 'student':
            return Result.objects.filter(student__user=user)
        return Result.objects.all()

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Attendance.objects.filter(course__teacher__user=user)
        elif user.user_type == 'student':
            return Attendance.objects.filter(student__user=user)
        return Attendance.objects.all()

class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [DjangoModelPermissions, IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'faculty':
            return Timetable.objects.filter(course__teacher__user=user)
        elif user.user_type == 'student':
            return Timetable.objects.filter(course__enrollment__student__user=user).distinct()
        return Timetable.objects.all()
