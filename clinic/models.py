from django.db import models

# Create your models here.

class Patients(models.Model):
    #  Patient model column 
    name = models.CharField(max_length=200,null=True)
    dateOFBirth = models.CharField(max_length=200, default='none', null=False)
    contactnumber = models.CharField(max_length=200,null=True)
    
    image = models.ImageField(null = True,blank = True)
    prescription = models.CharField(max_length=200,null= True)
    date= models.CharField(max_length=200, default='none', null=False)
    bill = models.IntegerField(null= True)

    def __str__(self):
        return self.name