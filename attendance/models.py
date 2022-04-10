from statistics import mode
from django.db import models
from student.models import Student
from courses.models import Course
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        
        # return " ".join([self.student.first_name, self.student.last_name, self.course.name])
        return "% s % s % s " %(self.student.first_name, self.student.last_name, self.course.name)
