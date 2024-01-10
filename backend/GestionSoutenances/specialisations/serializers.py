from rest_framework import serializers

from .models import Specialisations

class SpecialisationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialisations
        fields = '__all__'