from django.db import models

# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()