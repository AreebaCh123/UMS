from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




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

schema_view = get_schema_view(
   openapi.Info(
      title="University Management API",
      default_version='v1',
      description="API documentation for your UMS project",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
