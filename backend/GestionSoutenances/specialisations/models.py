from django.db import models
from datetime import datetime


# Create your models here.

class Specialisations(models.Model):
    name = models.CharField(max_length = 255)
    field = models.ForeignKey("field_of_study.FieldOfStudy", on_delete=models.CASCADE)
    professors = models.ManyToManyField("professors.Professors")
    is_deleted = models.BooleanField(default = False)
    date_deleting = models.DateField(null=True, blank=True, default=None)

    
    
    def __str__(self):
        return self.name
    
    def soft_delete(self):
        self.is_deleted = True
        self.date_deleting = datetime.now()
        self.save()
