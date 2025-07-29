from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import DepartmentViewSet, CourseViewSet, StudentViewSet, TeacherViewSet, EnrollmentViewSet, WithdrawalViewSet, ResultViewSet, AttendanceViewSet,TimetableViewSet
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'withdrawals', WithdrawalViewSet)
router.register(r'results',ResultViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'timetables', TimetableViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
