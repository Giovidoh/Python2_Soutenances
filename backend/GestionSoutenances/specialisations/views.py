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

#Liste des spécialisations
@api_view(['GET'])
def list(request):
    queryset = Specialisations.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = SpecialisatioinsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)


# Ajout d'une nouvelle spécialisation
@api_view(['POST'])
def add(request):
    serializer = SpecialisatioinsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la spécialisation existe déjà
        existing_field = Specialisations.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_field or existing_field.is_deleted == True):
            serializer.save()
            return Response({'message': 'Spécialisation ajoutée avec succès !', 'Spécialisations': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette spécialisation existe déjà ! Veuillez en créer une autre.'})


#### END CRUD ####