from rest_framework import serializers

from .models import SchoolYear

class SchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolYear
        fields = ['id', 'name']