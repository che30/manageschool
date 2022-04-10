from unicodedata import name
from django.db import models
from teacher.models import Teacher
from department.models import Department
class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=6, unique=True)
    course_credit = models.IntegerField(verbose_name="course credit")
    course_hours = models.IntegerField(verbose_name="course hours")
    def __str__(self):
        return self.name