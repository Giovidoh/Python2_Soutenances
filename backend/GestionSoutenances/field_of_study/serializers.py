from rest_framework import serializers

from .models import FieldOfStudy

class FieldOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldOfStudy
        fields = ['id', 'name']