# Importation du modèle
from datetime import datetime, timedelta
from .models import Defense

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import DefenseSerializer

# Create your views here.

# Liste des soutenances
@api_view(['GET'])
def list(request):
    queryset = Defense.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = DefenseSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout de soutenance
@api_view(['POST'])
def add(request):
    serializer = DefenseSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la soutenance existe déjà
        existing_defense = Defense.objects.filter(theme=request.data.get('theme'), date_time=request.data.get('date_time'), room=request.data.get('room'), student=request.data.get('student'), is_deleted=False).first()
        if (not existing_defense or existing_defense.is_deleted == True):
            ## Vérifier si la salle est disponible pour l'intervalle de temps choisi
            # Récupérer les soutenances du jour choisi
            defenses_of_the_day = Defense.objects.filter(date_time = request.data.get('date_time'))
            busy = False
            for defense in defenses_of_the_day:
                start_hour_db = datetime.hour(defense.date_time)
                duration_db = defense.duration
                end_hour_db = start_hour_db + timedelta(hours = duration_db)
                
                duration = 2
                if(request.data.get('duration')):
                    duration = request.data.get('duration')
                start_hour = datetime.hour(request.data.get('date_time'))
                end_hour = start_hour + timedelta(hours = duration)
                
                if(
                    (start_hour >= start_hour_db and start_hour <= end_hour_db)
                    or (end_hour >= start_hour_db and end_hour <= end_hour_db)
                    or (start_hour_db >= start_hour and start_hour_db <= end_hour)
                    or (end_hour_db >= start_hour and end_hour_db <= end_hour)
                ):
                    busy = True
            
            if(not busy):
                serializer.save()
                return Response({'message': 'Soutenance ajoutée avec succès !', 'defense': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Cette soutenance existe déjà ! Veuillez en créer une autre.'})
    
# Modification de soutenance
@api_view(['PUT'])
def update(request, id):
    defense = Defense.objects.filter(id=id).first()
    if (not defense or defense.is_deleted == True):
        return Response({'error': 'Cette soutenance n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DefenseSerializer(defense, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la filière existe déjà
        existing_defense = Defense.objects.filter(theme=request.data.get('theme'), date_time=request.data.get('date_time'), room=request.data.get('room'), student=request.data.get('student'), is_deleted=False).exclude(id=defense.id).first()
        if not existing_defense:
            serializer.save()
            return Response({'message': 'Soutenance modifiée avec succès !', 'defense': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Cette Soutenance existe déjà ! Veuillez en créer une autre.'})
        
# Suppression de soutenance
@api_view(['DELETE'])
def delete(request, id):
    defense = Defense.objects.filter(id=id).first()
    if (not defense or defense.is_deleted == True):
        return Response({'error': 'Cette soutenance n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si la soutenance existe faire une suppression logique
    defense.soft_delete()
    
    return Response({'message': 'Soutenance supprimée avec succès'}, status=status.HTTP_200_OK)