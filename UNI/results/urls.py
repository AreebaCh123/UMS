from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResultViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'results', ResultViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
