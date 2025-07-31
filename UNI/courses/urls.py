from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, TimetableViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'timetables', TimetableViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
