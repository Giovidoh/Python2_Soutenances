# Récupération du modèle
from .models import Professors

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import ProfessorsSerializer


# Create your views here.

#Liste des professeurs
@api_view(['GET'])
def list(request):
    queryset = Professors.objects.all()
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = ProfessorsSerializer(object).data
            result.append(serialized_data)
    
    return JsonResponse(result, safe = False)