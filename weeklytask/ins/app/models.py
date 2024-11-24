from django.db import models
# Create your models here.
class ins(models.Model):
    s_id=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    course=models.TextField()

class Course(models.Model):
    C_name=models.TextField()
    c_seats=models.IntegerField()

    
class Inscourses(models.Model):
    c_name=models.TextField()
    c_dis=models.TextField()