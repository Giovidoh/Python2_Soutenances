# Récupération du modèle
from .models import Student

from django.http import JsonResponse

# Importation de django_filters
from django_filters.rest_framework import DjangoFilterBackend

# Importations de rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics

# Importation du serializer
from .serializers import StudentSerializer, StudentsFilter

# Importation des fonctions personnalisées
from .functions import generate_serial_number



# Create your views here.

#### CRUD ####

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
    # Définir le numéro matricule de l'étudiant
    serial_number = generate_serial_number()
    request.data['serialNumber'] = serial_number
    
    serializer = StudentSerializer(data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si l'étudiant existe déjà (même nom, prénom, date de naissance)
        existing_student = Student.objects.filter(familyName=request.data.get('familyName'), firstName=request.data.get('firstName'), birth_date=request.data.get('birth_date'), is_deleted=False).first()
        if (not existing_student or existing_student.is_deleted == True):
            serializer.save()
            return Response({'message': 'Étudiant ajouté avec succès !', 'student': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Un étudiant ayant le même nom, prénom et date de naissance existe déjà ! Veuillez en ajouter un autre.'})

# Modification d'étudiant
@api_view(['PUT'])
def update(request, id):
    student = Student.objects.filter(id=id).first()
    if (not student or student.is_deleted == True):
        return Response({'error': 'Cet étudiant n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentSerializer(student, data=request.data)
    if(serializer.is_valid(raise_exception=True)):
        # Vérifier si l'étudiant existe déjà (même nom, prénom, date de naissance)
        existing_student = Student.objects.filter(familyName=request.data.get('familyName'), firstName=request.data.get('firstName'), birth_date=request.data.get('birth_date'), is_deleted=False).exclude(id=student.id).first()
        if not existing_student:
            serializer.save()
            return Response({'message': 'Étudiant modifié avec succès !', 'student': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Un étudiant ayant le même nom, prénom et date de naissance existe déjà ! Veuillez en ajouter un autre.'})
        
# Suppression d'étudiant
@api_view(['DELETE'])
def delete(request, id):
    student = Student.objects.filter(id=id).first()
    if (not student or student.is_deleted == True):
        return Response({'error': 'Cet étudiant n\'existe pas.'}, status=status.HTTP_404_NOT_FOUND)
    
    # Si l'étudiant existe faire une suppression logique
    student.soft_delete()
    
    return Response({'message': 'Étudiant supprimé avec succès'}, status=status.HTTP_200_OK)

#### END OF CRUD ####

#### OTHER VIEWS ####

#Filtre

class StudentsListFilter(generics.ListAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentsFilter


@api_view(['GET'])
def filter(request):
    query = request.GET.get('query', '')
    if query:
        queryset = Student.filter(query)
        result = [StudentSerializer(student).data for student in queryset]
        return Response(result)


#Recherche
class StudentsListSearch(generics.ListAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer
    search_fields = ['serialNumber', 'familyName', 'firstName', 'birth_date']


@api_view(['GET'])
def search(request):
    query = Student.objects.filter(is_deleted = False)
    if query:
        queryset = Student.filter(query)
        result = [StudentSerializer(student).data for student in queryset]
        return Response(result)


#### END OF OTHER VIEWS ####