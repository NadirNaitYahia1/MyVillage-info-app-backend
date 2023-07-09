from django.db import models

# Create your models here.



class Users(models.Model):
    user_mobile = models.CharField(primary_key=True,max_length=50)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name
    
class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE )
    bus_name = models.CharField(max_length=50)
    bus_time = models.TimeField()
    bus_date = models.DateField()
    bus_from = models.CharField(max_length=50)
    bus_to = models.CharField(max_length=50)
    bus_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.bus_name
    
    
class Pharmacies(models.Model):
    pharmacy_id = models.AutoField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE )
    pharmacy_name = models.CharField(max_length=50)
    pharmacy_address = models.CharField(max_length=50)
    pharmacy_image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.pharmacy_name


class Admin(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=50)
    def __str__(self):
        return self.admin_name





  
    # Autres champs de votre modèle

  