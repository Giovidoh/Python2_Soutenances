# Récupération du modèle
from .models import Student

from django.http import JsonResponse

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Importation du serializer
from .serializers import StudentSerializer


# Create your views here.

# Liste des étudiants
@api_view(['GET'])
def list(request):
    queryset = Student.objects.filter(is_deleted = False)
    result = []
    
    if queryset:
        for object in queryset:
            serialized_data = StudentSerializer(object).data
            result.append(serialized_data)
    
    return Response(result)

# Ajout d'étudiant
@api_view(['POST'])
def add(request):
    serializer = StudentSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si l'étudiant existe déjà (même nom, prénom, date de naissance)
        existing_field = Student.objects.filter(familyName=request.data.get('familyName'), firstName=request.data.get('firstName'), birth_date=request.data.get('birth_date'), is_deleted=False).first()
        if (not existing_field or existing_field.is_deleted == True):
            serializer.save()
            return Response({'message': 'Étudiant ajouté avec succès !', 'student': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Un étudiant ayant le même nom, prénom et date de naissance existe déjà ! Veuillez en ajouter un autre.'})
