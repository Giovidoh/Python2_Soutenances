from django.db import models

# Create your models here.

class Student(models.Model):
    familyName = models.CharField(max_length = 50)
    firstName = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 1)
    birth_date = models.DateField(auto_now_add = False, default = None)
    field_of_study = models.ForeignKey("field_of_study.FieldOfStudy", on_delete = models.CASCADE)
    school_year = models.ForeignKey("school_year.SchoolYear", on_delete = models.CASCADE)
    
    def __str__(self):
        return(self.familyName + " " + self.firstName)