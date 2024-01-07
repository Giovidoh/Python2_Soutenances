# Importation du modèle
from .models import Student

from datetime import datetime

# Fonction permettant de générer le numéro matricule du prochain étudiant à ajouter.
def generate_serial_number():
    # Récupérer l'année en cours.
    current_year = datetime.now().year
    
    # Compter le nombre d'étudiants enregistrés et ajouter 1
    number_of_students_plus_one = Student.objects.count() + 1
    
    # Rajouter des zéros aux emplacements vides si nécessaire
    first_part_of_serial_number = '{:04d}'.format(number_of_students_plus_one)
    
    # Retourner le numéro matricule
    serial_number = f"{first_part_of_serial_number}-{current_year}"
    return serial_number

generate_serial_number()