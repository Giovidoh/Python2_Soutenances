from django.db import models
from datetime import datetime

# Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=255)
    nbrePlace = models.IntegerField(default = 0)
    is_deleted = models.BooleanField(default = False)
    date_deleting = models.DateField(null=True, blank=True, default=None)
    
    def __str__(self):
        return self.name
    
    def soft_delete(self):
        self.is_deleted = True
        self.date_deleting = datetime.now()
        self.save()
        
    def filter(cls, query):
        return cls.objects.filter(name__icontains=query, is_deleted=False)