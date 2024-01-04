from django.db import models

# Create your models here.

class Defense(models.Model):
    theme = models.CharField(max_length = 255)
    date_time = models.DateTimeField(auto_now_add = False, default = None)
    result = models.IntegerField(default = None)
    room = models.ForeignKey('rooms.Rooms', on_delete = models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete = models.CASCADE)
    professors = models.ManyToManyField('professors.Professors')
    
    def __str__(self):
        return(self.theme)
    