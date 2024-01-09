# Récupération du modèle
from .models import Specialisations

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import SpecialisatioinsSerializer




#### CRUD ####

#Liste des professeurs
@api_view(['GET'])
def list(request):
    queryset = Specialisations.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = SpecialisatioinsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)


#### END CRUD ####