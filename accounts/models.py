from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email=models.EmailField(unique=True)

    ROLE_CHOICES=(
        ("ADMIN","ADMIN"),
        ("USER","USER")
    )

    role= models.CharField(max_length=10,choices=ROLE_CHOICES,default="USER")
    phone=models.CharField(max_length=15,blank=True)
    address=models.CharField(max_length=100,blank=True)
    
    

    def __str__(self):
        return self.email 
    