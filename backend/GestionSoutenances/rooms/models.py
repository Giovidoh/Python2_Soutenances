from django.db import models

# Create your models here.

class rooms(models.Model):
    nameRoom = models.CharField(max_length=255)
    availRoom = models.TextField(max_length=3, default = "yes") #Disponibilité de la salle
    
    def __str__(self):
        return self.nameRoom
    