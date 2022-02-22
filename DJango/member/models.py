from django.db import models

# Create your models here.

class Member(models.Model):
    
    u_firtname = models.CharField(max_length=32)
    u_lastname = models.CharField(max_length=32)
    u_eamil = models.EmailField(max_length=128,primary_key=True,unique=True)
    u_pw = models.CharField(max_length=64)
    u_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.u_firtname
    