# Récupération du modèle
from .models import Rooms

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import RoomsSerializer


# Create your views here.

#Liste des salles de soutenances
@api_view(['GET'])
def list(request):
    queryset = Rooms.objects.all()
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = RoomsSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout de salle
@api_view(['POST'])
def add(request):
    serializer = RoomsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la salle existe déjà
        existing_field = Rooms.objects.filter(name=request.data.get('name')).first()
        if not existing_field:
            serializer.save()
            return Response({'message': 'Salle ajoutée avec succès !', 'Rooms': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette salle existe déjà ! Veuillez en créer une autre.'})

# Modification de salle
@api_view(['PUT'])
def update(request, id):
    rooms = Rooms.objects.filter(id=id).first()
    if not rooms:
        return Response({'error': 'Cette salle n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoomsSerializer(rooms, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la salle existe déjà
        existing_field = Rooms.objects.filter(name=request.data.get('name')).exclude(id=rooms.id).first()
        if not existing_field:
            serializer.save()
            return Response({'message': 'Salle modifiée avec succès !', 'rooms': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette salle existe déjà ! Veuillez en créer une autre.'})