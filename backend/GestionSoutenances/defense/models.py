from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Defense(models.Model):
    theme = models.CharField(max_length = 255)
    date = models.DateField(default = None)
    time = models.TimeField(default = None)
    duration = models.IntegerField(default = 2)
    result = models.IntegerField(default = None, null = True)
    room = models.ForeignKey('rooms.Rooms', on_delete = models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete = models.CASCADE)
    professors = models.ManyToManyField('professors.Professors', through='DefenseProfessor')
    is_deleted = models.BooleanField(default = False)
    date_deleting = models.DateField(null=True, blank=True, default=None)
    
    def __str__(self):
        return(self.theme)
    
    def soft_delete(self):
        self.is_deleted = True
        self.date_deleting = datetime.now()
        self.save()
    
# Relation entre Soutenances et professeurs
class DefenseProfessor(models.Model):
    defense = models.ForeignKey(Defense, on_delete = models.CASCADE)
    professor = models.ForeignKey('professors.Professors', on_delete = models.CASCADE)
    mark = models.IntegerField(default = None, null = True, validators=[MinValueValidator(0), MaxValueValidator(20)])
    
    class Meta:
        unique_together = ('defense', 'professor')
    
    def __str__(self):
        return f"{self.defense} - {self.professor}"