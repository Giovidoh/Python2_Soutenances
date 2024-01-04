from django.db import models


# Create your models here.

class Specialisations(models.Model):
    name = models.CharField(max_length = 255)
    field = models.ForeignKey("field_of_study.FieldOfStudy", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name