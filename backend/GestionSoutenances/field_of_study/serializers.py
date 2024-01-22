from rest_framework import serializers
import django_filters


from .models import FieldOfStudy

class FieldsFilter(django_filters.FilterSet):
    class Meta:
        model = FieldOfStudy
        fields = ['name']

class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = ['id', 'name']