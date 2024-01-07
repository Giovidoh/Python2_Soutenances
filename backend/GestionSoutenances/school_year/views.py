# Récupération du modèle
from .models import SchoolYear

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import SchoolYearSerializer


# Create your views here.

# Liste des années d'étude
@api_view(['GET'])
def list(request):
    queryset = SchoolYear.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = SchoolYearSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout d'année d'étude
@api_view(['POST'])
def add(request):
    serializer = SchoolYearSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si l'année existe déjà
        existing_year = SchoolYear.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_year or existing_year.is_deleted == True):
            serializer.save()
            return Response({'message': 'Année ajoutée avec succès !', 'school_year': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette année existe déjà ! Veuillez en créer une autre.'})
    
# Modification d'année d'étude
@api_view(['PUT'])
def update(request, id):
    school_year = SchoolYear.objects.filter(id=id).first()
    if (not school_year or school_year.is_deleted == True):
        return Response({'error': 'Cette année n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = SchoolYearSerializer(school_year, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si l'année existe déjà
        existing_year = SchoolYear.objects.filter(name=request.data.get('name')).exclude(id=school_year.id).first()
        if not existing_year:
            serializer.save()
            return Response({'message': 'Année modifiée avec succès !', 'school_year': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette année existe déjà ! Veuillez en créer une autre.'})
        
# Suppression d'année d'étude
@api_view(['DELETE'])
def delete(request, id):
    school_year = SchoolYear.objects.filter(id=id).first()
    if (not school_year or school_year.is_deleted == True):
        return Response({'error': 'Cette année n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si l'année existe faire une suppression logique
    school_year.soft_delete()
    
    return Response({'message': 'Année supprimée avec succès'}, status=status.HTTP_200_OK)