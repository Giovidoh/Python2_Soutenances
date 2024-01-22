# Récupération du modèle
from .models import FieldOfStudy

from django.http import JsonResponse

# Importation de django_filters
from django_filters.rest_framework import DjangoFilterBackend


# Importations de rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


# Importation du serializer
from .serializers import FieldOfStudySerializer, FieldsFilter


# Create your views here.

# Liste des filières
@api_view(['GET'])
def list(request):
    queryset = FieldOfStudy.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = FieldOfStudySerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout de filière
@api_view(['POST'])
def add(request):
    serializer = FieldOfStudySerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la filière existe déjà
        existing_field = FieldOfStudy.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_field or existing_field.is_deleted == True):
            serializer.save()
            return Response({'message': 'Filière ajoutée avec succès !', 'field_of_study': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette filière existe déjà ! Veuillez en créer une autre.'})
    
# Modification de filière
@api_view(['PUT'])
def update(request, id):
    field_of_study = FieldOfStudy.objects.filter(id=id).first()
    if (not field_of_study or field_of_study.is_deleted == True):
        return Response({'error': 'Cette filière n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FieldOfStudySerializer(field_of_study, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la filière existe déjà
        existing_field = FieldOfStudy.objects.filter(name=request.data.get('name')).exclude(id=field_of_study.id).first()
        if not existing_field:
            serializer.save()
            return Response({'message': 'Filière modifiée avec succès !', 'field_of_study': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette filière existe déjà ! Veuillez en créer une autre.'})
        
# Suppression de filière
@api_view(['DELETE'])
def delete(request, id):
    field_of_study = FieldOfStudy.objects.filter(id=id).first()
    if (not field_of_study or field_of_study.is_deleted == True):
        return Response({'error': 'Cette filière n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si la filière existe faire une suppression logique
    field_of_study.soft_delete()
    
    return Response({'message': 'Filière supprimée avec succès'}, status=status.HTTP_200_OK)


#### OTHER VIEWS ####


#Filtre

class FieldsListFilter(generics.ListAPIView):
    queryset = FieldOfStudy.objects.filter(is_deleted=False)
    serializer_class = FieldOfStudySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FieldsFilter


@api_view(['GET'])
def filter(request):
    query = request.GET.get('query', '')
    if query:
        queryset = FieldOfStudy.filter(query)
        result = [FieldOfStudySerializer(room).data for room in queryset]
        return Response(result)


#Recherche
class FieldsListSearch(generics.ListAPIView):
    queryset = FieldOfStudy.objects.filter(is_deleted=False)
    serializer_class = FieldOfStudySerializer
    search_fields = ['name']


@api_view(['GET'])
def search(request):
    query = FieldOfStudy.objects.filter(is_deleted = False)
    if query:
        queryset = FieldOfStudy.filter(query)
        result = [FieldOfStudySerializer(room).data for room in queryset]
        return Response(result)

#### END OF OTHER VIEWS ####