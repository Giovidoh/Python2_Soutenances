from rest_framework import serializers

from .models import Professors
import django_filters


class ProfessorsFilter(django_filters.FilterSet):
    class Meta:
        model = Professors
        fields = ['name', 'firstName', 'email', 'contact', 'address']


class ProfessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = '__all__'