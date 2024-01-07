from rest_framework import serializers
from .models import Student

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