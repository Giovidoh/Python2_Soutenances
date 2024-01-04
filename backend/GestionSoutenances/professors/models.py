from django.db import models

# Create your models here.

class Professors(models.Model):
    name = models.CharField(max_length = 30)
    firstName = models.CharField(max_length = 255)
    contact = models.CharField(max_length = 8)
    email = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    experience = models.IntegerField(default = 0) #Nombre de soutenances assitées par le professeur
    
    def __str__(self):
        return self.name + " " + self.firstName + " " + self.email