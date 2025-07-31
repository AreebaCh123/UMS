from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Course, Timetable
from .serializers import CourseSerializer, TimetableSerializer

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
