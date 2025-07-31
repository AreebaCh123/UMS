from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Result, Attendance
from .serializers import ResultSerializer, AttendanceSerializer

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
