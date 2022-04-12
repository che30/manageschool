from django.db import models
from department.models import Department
# Create your models here.
class Teacher(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name="first name", max_length=32)
    last_name = models.CharField(verbose_name="last name", max_length=32)
    institutional_email = models.EmailField(verbose_name="institutional email",
     max_length=32, unique=True, null=False)
    def __str__(self):
        return" %s %s " %(self.first_name , self.last_name)
