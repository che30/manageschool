from django.forms import ModelForm,ModelChoiceField
from attendance.models import Attendance
from courses.models import Course
# from student.models import Student
# from courses.models import Course
class AttendanceForm(ModelForm):
    all_courses = Course.objects.all()
    course = ModelChoiceField(queryset= all_courses, empty_label=" ")
    class Meta:
        model = Attendance
        fields = ('student','course')
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['course']= ModelChoiceField(queryset=Course.objects.all())
        # self.fields['course'].queryset = Course.objects.all()
