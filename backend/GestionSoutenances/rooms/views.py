# Récupération du modèle
from .models import Rooms

from django.http import JsonResponse

# Importations de rest_framework
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

# Ajout de salles
@api_view(['POST'])
def add(request):
    serializer = RoomsSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        serializer.save()
        return Response({'message': 'Salle ajoutée avec succès !', 'Salle': serializer.data})
