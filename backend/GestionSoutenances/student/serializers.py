from rest_framework import serializers
from .models import Student
import django_filters


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['serialNumber', 'familyName', 'firstName', 'birth_date']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'serialNumber',
            'familyName',
            'firstName',
            'gender',
            'birth_date',
            'field_of_study',
            'school_year',
        ]