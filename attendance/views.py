
from django import forms
from django.shortcuts import redirect, render
from attendance.forms import AttendanceForm
from attendance.models import Attendance
from account.models import Account
from student.models import Student
def new_attendance_view(request):
    context = {}

    # form = AttendanceForm(request.POST)
    form = AttendanceForm()
    student_email = Account.objects.get(pk =request.user.id).email
    print(student_email)
    student_instance = Student.objects.get(institutional_email = student_email)
    form.fields['student'].initial = student_instance
    form.fields['student'].widget = forms.HiddenInput()
    context['form'] = form
    return render(request, 'attendance/attend.html', context)
def create_new_attendance(request):
     if request.user.is_authenticated == False:
        return redirect('login')
     form = AttendanceForm(request.POST)
     if form.is_valid():
        student_instance = form.cleaned_data.get('student')
        course_instance = form.cleaned_data.get('course')
        new_attendance = Attendance(student = student_instance, course= course_instance)
        new_attendance.save()
     return redirect('show', pk=request.user.id)
