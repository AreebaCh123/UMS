from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import Student
from enrollments.models import Enrollment, Withdrawal
from results.models import Result, Attendance
from django.db.models import Count, Avg, F
from datetime import datetime
from django.db.models import Q
from accounts.models import Teacher




class TotalStudentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = Student.objects.count()
        return Response({"total_students": total})



class StudentsByDepartmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Student.objects.values(dept_name=F('department__name')).annotate(count=Count('id'))
        return Response(data)


# ✅ 3. Students grouped by enrollment year
class StudentsByEnrollmentYearView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Student.objects.annotate(
            year=F('enrollment_date__year')
        ).values('year').annotate(count=Count('id'))
        return Response(data)
    
class TotalFacultyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total = Teacher.objects.count()
        return Response({"total_faculty": total})
    
from django.db.models import Count, F

class FacultyByDepartmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Teacher.objects.values(dept_name=F('department__name')).annotate(count=Count('id'))
        return Response(data)


from courses.models import Course

class FacultyCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, teacher_id):
        courses = Course.objects.filter(teacher_id=teacher_id).values('name', 'code')
        return Response({"teacher_id": teacher_id, "courses": list(courses)})



# ✅ 4. Full analytics for a specific student
class StudentDetailAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

    
        gpa = Result.objects.filter(student=student).aggregate(gpa=Avg('grade'))['gpa']

        total_attendance = Attendance.objects.filter(student=student).count()
        present_attendance = Attendance.objects.filter(student=student, status='present').count()
        attendance_percent = (present_attendance / total_attendance) * 100 if total_attendance else 0

     
        courses = Enrollment.objects.filter(student=student).values('course__name', 'course__code')

     
        withdrawals = Withdrawal.objects.filter(student=student).values('course__name', 'date', 'reason')

        return Response({
            "student_id": student.id,
            "gpa": round(gpa, 2) if gpa is not None else None,
            "attendance_percent": round(attendance_percent, 2),
            "courses_enrolled": list(courses),
            "withdrawal_history": list(withdrawals)
        })
class TopPerformingStudentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        top_students = Result.objects.values(
            'student__id',
        ).annotate(gpa=Avg('grade')).order_by('-gpa')[:10]
        return Response(top_students)
class CourseWiseGPAView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        course_gpa = Result.objects.values(
            course_name=F('course__name')
        ).annotate(avg_gpa=Avg('grade')).order_by('-avg_gpa')
        return Response(course_gpa)
class MostEnrolledCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        courses = Enrollment.objects.values(
            course_name=F('course__name')
        ).annotate(enroll_count=Count('id')).order_by('-enroll_count')
        return Response(courses)
class MostAbsentStudentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Attendance.objects.filter(status='absent').values(
            'student__id',
          
        ).annotate(absences=Count('id')).order_by('-absences')[:10]
        return Response(data)
class WithdrawalsByCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Withdrawal.objects.values(
            course_name=F('course__name')
        ).annotate(withdrawal_count=Count('id')).order_by('-withdrawal_count')
        return Response(data)
class AttendanceSummaryByCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = Attendance.objects.values(
            course_name=F('course__name')
        ).annotate(
            total_classes=Count('id'),
            presents=Count('id', filter=Q(status='present')),
            absents=Count('id', filter=Q(status='absent')),
        )
        return Response(data)

