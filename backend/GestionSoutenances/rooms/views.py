# Récupération du modèle
from .models import Rooms

from django.http import JsonResponse

# Importation de django_filters
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

# Importations de rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import generics

# Importation du serializer
from .serializers import RoomsSerializer, RoomsFilter

# Create your views here.

#### CRUD ####

#Liste des salles de soutenances
@api_view(['GET'])
def list(request):
    queryset = Rooms.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = RoomsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout de nouvelle salle
@api_view(['POST'])
def add(request):
    serializer = RoomsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la salle existe déjà
        existing_room = Rooms.objects.filter(name=request.data.get('name'), is_deleted=False).first()
        if (not existing_room or existing_room.is_deleted == True):
            serializer.save()
            return Response({'message': 'Salle ajoutée avec succès !', 'rooms': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette salle existe déjà ! Veuillez en créer une autre.'})
    
# Modification de salle
@api_view(['PUT'])
def update(request, id):
    rooms = Rooms.objects.filter(id=id).first()
    if (not rooms or rooms.is_deleted == True):
        return Response({'error': 'Cette salle n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoomsSerializer(rooms, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la salle existe déjà
        existing_room = Rooms.objects.filter(name=request.data.get('name')).exclude(id=rooms.id).first()
        if not existing_room:
            serializer.save()
            return Response({'message': 'Salle modifiée avec succès !', 'rooms': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette salle existe déjà ! Veuillez saisir un autre nom.'})
        
# Suppression de salle
@api_view(['DELETE'])
def delete(request, id):
    rooms = Rooms.objects.filter(id=id).first()
    if (not rooms or rooms.is_deleted == True):
        return Response({'error': 'Cette salle n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si la salle existe faire une suppression logique
    rooms.soft_delete()
    
    return Response({'message': 'Salle supprimée avec succès'}, status=status.HTTP_200_OK)

#### END OF CRUD ####

#### OTHER VIEWS ####

class RoomsList(generics.ListAPIView):
    queryset = Rooms.objects.filter(is_deleted=False)
    serializer_class = RoomsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomsFilter


@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')
    if query:
        queryset = Rooms.search(query)
        result = [RoomsSerializer(room).data for room in queryset]
        return Response(result)



#### END OF OTHER VIEWS ####