# Récupération du modèle
from .models import Specialisations

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import SpecialisationsSerializer




#### CRUD ####

#Liste des spécialisations
@api_view(['GET'])
def list(request):
    queryset = Specialisations.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = SpecialisationsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)


# Ajout d'une nouvelle spécialisation
@api_view(['POST'])
def add(request):
    serializer = SpecialisationsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la spécialisation existe déjà
        existing_soutenance = Specialisations.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_soutenance or existing_soutenance.is_deleted == True):
            serializer.save()
            return Response({'message': 'Spécialisation ajoutée avec succès !', 'Spécialisations': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette spécialisation existe déjà ! Veuillez en créer une autre.'})


# Modification d'une spécialisation
@api_view(['PUT'])
def update(request, id):
    specialisations = Specialisations.objects.filter(id=id).first()
    if (not specialisations or specialisations.is_deleted == True):
        return Response({'error': 'Désolé, cette spécialité n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SpecialisationsSerializer(specialisations, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la spécialisation existe déjà
        existing_soutenance = Specialisations.objects.filter(name=request.data.get('name'), field=request.data.get('field')).exclude(id=specialisations.id).first()
        if not existing_soutenance:
            serializer.save()
            return Response({'message': 'Spécialisation modifié avec succès !', 'professors': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette spécialisation existe déjà ! Veuillez saisir un autre nom.'})


# Suppression d'une spécialisation
@api_view(['DELETE'])
def delete(request, id):
    specialisations = Specialisations.objects.filter(id=id).first()
    if (not specialisations or specialisations.is_deleted == True):
        return Response({'error': 'Désolé, cette spécialité n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si la spécialisation existe faire une suppression logique
    specialisations.soft_delete()
    
    return Response({'message': 'Spécialité supprimée avec succès'}, status=status.HTTP_200_OK)


#### END CRUD ####