from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=32, verbose_name="First name")
    last_name = models.CharField(max_length=32, verbose_name="Last name")
    registration_number = models.CharField(max_length=8, verbose_name="Registration number", unique=True )
    date_of_birth = models.DateField(verbose_name="date of birth")
    email = models.EmailField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + self.last_name
