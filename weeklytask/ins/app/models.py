from django.db import models
# Create your models here.


    
class Inscourses(models.Model):
    c_id=models.TextField()
    c_name=models.TextField()
    c_dis=models.TextField()
    img=models.FileField()
    duration=models.TextField()

class Message(models.Model):
    name=models.TextField()
    email=models.EmailField()
    message=models.TextField()