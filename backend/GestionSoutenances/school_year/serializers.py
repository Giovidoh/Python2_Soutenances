from rest_framework import serializers
import django_filters


from .models import SchoolYear

class YearsFilter(django_filters.FilterSet):
    class Meta:
        model = SchoolYear
        fields = ['name']

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name']