from django.urls import path

from .views import (
    TotalStudentsView,
    StudentsByDepartmentView,
    StudentsByEnrollmentYearView,
    StudentDetailAnalyticsView,
     TopPerformingStudentsView,CourseWiseGPAView,
    MostEnrolledCoursesView, MostAbsentStudentsView, WithdrawalsByCourseView,
    AttendanceSummaryByCourseView,
      TotalFacultyView,
    FacultyByDepartmentView,
    FacultyCoursesView,
    
)

urlpatterns = [
    path('students/total/', TotalStudentsView.as_view(), name='total-students'),
    path('students/by-department/', StudentsByDepartmentView.as_view(), name='students-by-department'),
    path('students/by-enrollment-year/', StudentsByEnrollmentYearView.as_view(), name='students-by-enrollment-year'),
    path('students/<int:student_id>/analytics/', StudentDetailAnalyticsView.as_view(), name='student-analytics'),
    path('students/top-gpa/', TopPerformingStudentsView.as_view()),
    path('courses/gpa/', CourseWiseGPAView.as_view()),
    path('courses/most-enrolled/', MostEnrolledCoursesView.as_view()),
    path('students/most-absent/', MostAbsentStudentsView.as_view()),
    path('withdrawals/by-course/', WithdrawalsByCourseView.as_view()),
    path('faculty/total/', TotalFacultyView.as_view()),
    path('faculty/by-department/', FacultyByDepartmentView.as_view()),
    path('faculty/<int:teacher_id>/courses/', FacultyCoursesView.as_view()),

]
