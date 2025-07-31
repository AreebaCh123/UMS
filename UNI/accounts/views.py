from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Student, Teacher

from .serializers import StudentSerializer, TeacherSerializer

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
