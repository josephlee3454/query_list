from django.db import models

# Create your models here.



class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(max_length= 255)
    age = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email + " " + self.age + f'{self.id}'