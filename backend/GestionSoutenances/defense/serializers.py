from rest_framework import serializers
from .models import Defense, DefenseProfessor
import django_filters


class DefensesFilter(django_filters.FilterSet):
    class Meta:
        model = Defense
        fields = ['theme', 'date', 'result', 'duration']


class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = '__all__'

class DefenseProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseProfessor
        fields = '__all__'