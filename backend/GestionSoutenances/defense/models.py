from django.db import models

# Create your models here.

class Defense(models.Model):
    theme = models.CharField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add = False, default = None)
    result = models.IntegerField(default = None)
    room = models.ForeignKey('rooms.Rooms', on_delete = models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete = models.CASCADE)
    professors = models.ManyToManyField('professors.Professors', through='DefenseProfessor')
    
    def __str__(self):
        return(self.theme)
    
# Relation entre Soutenances et professeurs
class DefenseProfessor(models.Model):
    defense = models.ForeignKey(Defense, on_delete = models.CASCADE)
    professor = models.ForeignKey('professors.Professors', on_delete = models.CASCADE)
    mark = models.IntegerField(default = None, null = True)
    
    def __str__(self):
        return f"{self.defense} - {self.professor}"