from django.db import models

# Create your models here.

class SchoolYear:
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return(self.name)