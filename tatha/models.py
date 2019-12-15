from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=30)


    def __str__(self):
        return self.email

class Register(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class  Send(models.Model):
       email = models.EmailField(max_length=30)
       password = models.CharField(max_length=10)

       def __str__(self):
           return self.email




