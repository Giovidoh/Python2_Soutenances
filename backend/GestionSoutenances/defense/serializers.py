from rest_framework import serializers
from .models import Defense, DefenseProfessor

class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = '__all__'

class DefenseProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseProfessor
        fields = '__all__'