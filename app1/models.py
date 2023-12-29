from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User1(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Complaintboarder(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    complaint_text = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name

class Complaintcyber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    complaint_text = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Complaintterror(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    complaint_text = models.TextField()
    uploaded_file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name    