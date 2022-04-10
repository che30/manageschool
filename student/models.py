from django.db import models
from department.models import Department
class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name="First name")
    last_name = models.CharField(max_length=32, verbose_name="Last name")
    matricule_number = models.CharField(max_length=8, verbose_name="Matricule number", unique=True )
    date_of_birth = models.DateField(verbose_name="date of birth")
    email = models.EmailField(max_length=32, unique=True)
    institutional_email = models.EmailField(max_length=32, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "% s % s " %(self.first_name,self.last_name)