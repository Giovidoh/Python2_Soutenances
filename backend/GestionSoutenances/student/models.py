from django.db import models
from datetime import datetime

# Create your models here.

class Student(models.Model):
    serialNumber = models.CharField(max_length = 9, default = None)
    familyName = models.CharField(max_length = 50)
    firstName = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 1)
    birth_date = models.DateField(auto_now_add = False, default = None)
    field_of_study = models.ForeignKey("field_of_study.FieldOfStudy", on_delete = models.CASCADE)
    school_year = models.ManyToManyField("school_year.SchoolYear")
    is_deleted = models.BooleanField(default = False)
    date_deleting = models.DateField(null=True, blank=True, default=None)
    
    def __str__(self):
        return(self.familyName + " " + self.firstName)
    
    def soft_delete(self):
        self.is_deleted = True
        self.date_deleting = datetime.now()
        self.save()