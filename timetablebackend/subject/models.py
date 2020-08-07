from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_code = models.CharField(max_length=6)
    subject_name = models.CharField(max_length=50)
    lecturer = models.CharField(max_length=50)
    room = models.CharField(max_length=10)
    day = models.CharField(max_length=3)
    starttime = models.CharField(max_length=5)
    endtime = models.CharField(max_length=5)
    color = models.CharField(max_length=9)