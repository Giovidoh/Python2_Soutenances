from rest_framework import serializers
import django_filters

from .models import Rooms

class RoomsFilter(django_filters.FilterSet):
    class Meta:
        model = Rooms
        fields = ['name']

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'