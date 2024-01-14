from rest_framework import serializers
from .models import Defense

class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = '__all__'