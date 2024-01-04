from django.db import models
from field_of_study import FieldOfStudy

# Create your models here.

class Specialisations(models.Model):
    name = models.CharField(max_length = 255)
    field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name