from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Enrollment, Withdrawal
from .serializers import EnrollmentSerializer, WithdrawalSerializer

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
