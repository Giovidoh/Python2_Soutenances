from django.db import models
from datetime import datetime

# Create your models here.

class Professors(models.Model):
    name = models.CharField(max_length = 30)
    firstName = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 8)
    email = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    experience = models.IntegerField(default = 0) #Nombre de soutenances assitées par le professeur
    is_deleted = models.BooleanField(default = False)
    date_deleting = models.DateField(null=True, blank=True, default=None)
    fieldOfStudy = models.ManyToManyField("field_of_study.FieldOfStudy")

    
    def __str__(self):
        return self.name + " " + self.firstName + " " + self.email
    
    def soft_delete(self):
        self.is_deleted = True
        self.date_deleting = datetime.now()
        self.save()
