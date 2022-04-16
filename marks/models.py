from django.db import models
from attendance.models import Attendance
from student.models import Student
from courses.models import Course 

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # semester_one = models.IntegerField(verbose_name="first semester", default=0)
    # semeter_two = models.IntegerField(verbose_name="second semeseter", default=0)
    ca = models.IntegerField(verbose_name=" continuous assesment",default=0)
    exam = models.IntegerField(verbose_name="Exams assesment",default=0)
    resit = models.IntegerField(verbose_name="Resit",default=0)
    total = models.IntegerField(verbose_name='total',default=0)
    grade = models.CharField(max_length=1, default=None)
    def __str__(self):
        return"%s %s %s %s %s" %(self.student.first_name,
         self.student.last_name,
         self.student.matricule_number, self.total, self.grade)
