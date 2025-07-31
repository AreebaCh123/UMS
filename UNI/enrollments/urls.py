from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet, WithdrawalViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'withdrawals', WithdrawalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
