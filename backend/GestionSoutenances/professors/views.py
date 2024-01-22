# Récupération du modèle
from .models import Professors

from django.http import JsonResponse

# Importation de django_filters
from django_filters.rest_framework import DjangoFilterBackend

# Importations de rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


# Importation du serializer
from .serializers import ProfessorsSerializer, ProfessorsFilter


# Create your views here.

#### CRUD ####

#Liste des professeurs
@api_view(['GET'])
def list(request):
    queryset = Professors.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = ProfessorsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout d'un nouveau professeur
@api_view(['POST'])
def add(request):
    serializer = ProfessorsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si le professeur existe déjà
        existing_professor = Professors.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_professor or existing_professor.is_deleted == True):
            serializer.save()
            return Response({'message': 'Professeur ajouté avec succès !', 'Professors': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Ce professeur existe déjà ! Veuillez en créer un autre.'})

# Modification d'un professeur
@api_view(['PUT'])
def update(request, id):
    professors = Professors.objects.filter(id=id).first()
    if (not professors or professors.is_deleted == True):
        return Response({'error': 'Désolé, ce professeur n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProfessorsSerializer(professors, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si le professeur existe déjà
        existing_professor = Professors.objects.filter(name=request.data.get('name'), firstName=request.data.get('firstName'), email=request.data.get('email')).exclude(id=professors.id).first()
        if not existing_professor:
            serializer.save()
            return Response({'message': 'Professeur modifié avec succès !', 'professors': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Ce professeur existe déjà ! Veuillez saisir un autre nom.'})

# Suppression d'un professeur
@api_view(['DELETE'])
def delete(request, id):
    professors = Professors.objects.filter(id=id).first()
    if (not professors or professors.is_deleted == True):
        return Response({'error': 'Désolé, ce professeur n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si le professeur existe faire une suppression logique
    professors.soft_delete()
    
    return Response({'message': 'Professeur supprimé avec succès'}, status=status.HTTP_200_OK)

#### END OF CRUD ####

#### OTHER VIEWS ####

#Affichage de tous les professeurs supprimés
@api_view(['GET'])
def deletedProfList(request):
    queryset = Professors.objects.filter(is_deleted = True)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = ProfessorsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

#Filtre

class ProfessorsListFilter(generics.ListAPIView):
    queryset = Professors.objects.filter(is_deleted=False)
    serializer_class = ProfessorsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfessorsFilter


@api_view(['GET'])
def filter(request):
    query = request.GET.get('query', '')
    if query:
        queryset = Professors.filter(query)
        result = [ProfessorsSerializer(professor).data for professor in queryset]
        return Response(result)


#Recherche
class ProfessorsListSearch(generics.ListAPIView):
    queryset = Professors.objects.filter(is_deleted=False)
    serializer_class = ProfessorsSerializer
    search_fields = ['name', 'firstName', 'email', 'contact', 'address']


@api_view(['GET'])
def search(request):
    query = Professors.objects.filter(is_deleted = False)
    if query:
        queryset = Professors.filter(query)
        result = [ProfessorsSerializer(professor).data for professor in queryset]
        return Response(result)


#### END OF OTHER VIEWS ####