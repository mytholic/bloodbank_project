from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Data(models.Model):
    username=models.CharField(max_length=300)
    address=models.CharField(max_length=300)
    sex=models.CharField(max_length=300)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.username

sex_choice=(('male','MALE'),('female','FEMALE'))
blood_group_choice=(('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),("o+",'O+'),('o-','O-'),('ab+','AB+'),('ab-','AB-'))

class Snippet(models.Model):
    name=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    email=models.EmailField()
    phone_number=models.IntegerField()
    sex=models.CharField(max_length=100,choices=sex_choice,default='MALE')
    blood_group=models.CharField(max_length=100,choices=blood_group_choice,default='A+')
    pre_existing_diseases=models.TextField()

    def __str__(self):
        return self.name