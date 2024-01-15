# Importation du modèle
from datetime import datetime, timedelta

from .models import Defense
from rooms.models import Rooms
from student.models import Student
from professors.models import Professors

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
            
            # Nom de la salle
            room_name = Rooms.objects.filter(id = serialized_data['room']).first().name
            serialized_data['room_name'] = room_name
            
            # Nom & prénom de l'étudiant
            student = Student.objects.filter(id = serialized_data['student']).first()
            student_family_name = student.familyName
            student_first_name = student.firstName
            serialized_data['student_name'] = student_family_name.upper() + ' ' + student_first_name
            
            # Noms et prénoms des professeurs
            if(serialized_data['professors']):
                professors = serialized_data['professors']
                professors_names = []
                for professor in professors:
                    professor = Professors.objects.filter(id = professor).first()
                    professor_name = professor.name
                    professor_first_name = professor.firstName
                    
                    professors_names = professor_name.upper() + ' ' + professor_first_name
                
                serialized_data['professors_names'] = professors_names
                
            
            result.append(serialized_data)
    
    return Response(result)


# Ajout de soutenance
@api_view(['POST'])
def add(request):
    serializer = DefenseSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si la soutenance existe déjà
        existing_defense = Defense.objects.filter(theme=request.data.get('theme'),
                                                  date=request.data.get('date'),
                                                  time=request.data.get('time'),
                                                  room=request.data.get('room'),
                                                  student=request.data.get('student'),
                                                  is_deleted=False).first()
        if (not existing_defense or existing_defense.is_deleted == True):
            ## Vérifier si la salle est disponible pour l'intervalle de temps choisi
            # Récupérer les soutenances du jour choisi et qui ne sont pas supprimées
            defenses_of_the_day = Defense.objects.filter(date = request.data.get('date'), is_deleted = False)
            
            # Initialiser la variable d'occupation et les tableaux des heures d'indisponibilité
            busy = False
            busy_starts_hours = []
            busy_ends_hours = []
            
            if(defenses_of_the_day):
                
                # Récupérer l'heure de début renseignée et calculer l'heure de fin
                # Utiliser la durée renseignée, sinon utiliser la durée par défaut
                duration = 2
                if(request.data.get('duration')):
                    duration = request.data.get('duration')
                start_hour = request.data.get('time')
                end_hour = (datetime.strptime(start_hour, '%H:%M:%S') + timedelta(hours = duration)).strftime('%H:%M:%S')
                
                # Pour chaque soutenance de la base de données effectuer les opérations suivantes
                for defense in defenses_of_the_day:
                    # Récupérer l'heure de début et calculer l'heure de fin de la soutenance de la bdd
                    start_hour_db = defense.time.strftime('%H:%M:%S')
                    duration_db = defense.duration
                    end_hour_db = (datetime.strptime(start_hour_db, '%H:%M:%S') + timedelta(hours = duration_db)).strftime('%H:%M:%S')
                    
                    # Récupérer les heure de début et de fin dans les tableaux
                    busy_starts_hours.append(start_hour_db)
                    busy_ends_hours.append(end_hour_db)
                    
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
                    room_id = request.data.get('room')
                    room_name = Rooms.objects.filter(id = room_id).first().name
                    return Response({
                                'error': f"La salle '{room_name}' est indisponible à cette heure!",
                                'busy_starts_hours': busy_starts_hours,
                                'busy_ends_hours': busy_ends_hours,
                            })
                    
            # Si aucune soutenance n'est programmée dans la journée, enregistrer la nouvelle.
            else: 
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
        # Vérifier si la soutenance existe déjà SAUF CELLE A MODIFIER
        existing_defense = Defense.objects.filter(theme=request.data.get('theme'),
                                                  date=request.data.get('date'),
                                                  time=request.data.get('time'),
                                                  room=request.data.get('room'),
                                                  student=request.data.get('student'),
                                                  is_deleted=False).exclude(id = id).first()
        if not existing_defense:
            ## Vérifier si la salle est disponible pour l'intervalle de temps choisi
            # Récupérer les soutenances du jour choisi et qui ne sont pas supprimées
            # SAUF CELLE A MODIFIER
            defenses_of_the_day = Defense.objects.filter(date = request.data.get('date'), is_deleted = False).exclude(id = id)
            
            # Initialiser la variable d'occupation et les tableaux des heures d'indisponibilité
            busy = False
            busy_starts_hours = []
            busy_ends_hours = []
            
            if(defenses_of_the_day):
                
                # Récupérer l'heure de début renseignée et calculer l'heure de fin
                # Utiliser la durée renseignée, sinon utiliser la durée par défaut
                duration = 2
                if(request.data.get('duration')):
                    duration = request.data.get('duration')
                start_hour = request.data.get('time')
                end_hour = (datetime.strptime(start_hour, '%H:%M:%S') + timedelta(hours = duration)).strftime('%H:%M:%S')
                
                # Pour chaque soutenance de la base de données effectuer les opérations suivantes
                for defense in defenses_of_the_day:
                    # Récupérer l'heure de début et calculer l'heure de fin de la soutenance de la bdd
                    start_hour_db = defense.time.strftime('%H:%M:%S')
                    duration_db = defense.duration
                    end_hour_db = (datetime.strptime(start_hour_db, '%H:%M:%S') + timedelta(hours = duration_db)).strftime('%H:%M:%S')
                    
                    # Récupérer les heure de début et de fin dans les tableaux
                    busy_starts_hours.append(start_hour_db)
                    busy_ends_hours.append(end_hour_db)
                    
                    if(
                        (start_hour >= start_hour_db and start_hour <= end_hour_db)
                        or (end_hour >= start_hour_db and end_hour <= end_hour_db)
                        or (start_hour_db >= start_hour and start_hour_db <= end_hour)
                        or (end_hour_db >= start_hour and end_hour_db <= end_hour)
                    ):
                        busy = True
                    
                if(not busy):
                    serializer.save()
                    return Response({'message': 'Soutenance modifiée avec succès !', 'defense': serializer.data}, status=status.HTTP_200_OK)
                else:
                    room_id = request.data.get('room')
                    room_name = Rooms.objects.filter(id = room_id).first().name
                    return Response({
                                'error': f"La salle '{room_name}' est indisponible à cette heure!",
                                'busy_starts_hours': busy_starts_hours,
                                'busy_ends_hours': busy_ends_hours,
                            })
                    
            # Si aucune soutenance n'est enregistrée dans la journée, effectuer les modifications
            else:
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