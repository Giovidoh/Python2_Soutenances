# Récupération du modèle
from .models import FieldOfStudy

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import FieldOfStudySerializer


# Create your views here.

# Liste des filières
@api_view(['GET'])
def list(request):
    queryset = FieldOfStudy.objects.all()
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = FieldOfStudySerializer(object).data
            result.append(serialized_data)
    
    return JsonResponse(result, safe = False)