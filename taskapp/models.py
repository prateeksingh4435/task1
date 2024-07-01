from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_patient = models.BooleanField(default = False)
    is_doctor = models.BooleanField(default = False)
    
    
    
class signup(models.Model):
    
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length=128)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    
    
    def __str__(self):
        return self.first_name