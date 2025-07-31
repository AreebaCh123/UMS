from django_filters import rest_framework as filters
class StudentFilter(filters.FilterSet):
    enrollment_year = filters.NumberFilter(field_name='enrollment_date', lookup_expr='year')
    course = filters.NumberFilter(field_name='enrollment__course')

    class Meta:
        model = Student
        fields = ['enrollment_date', 'enrollment_year', 'course']
