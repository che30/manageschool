
from django import forms
from django.shortcuts import redirect, render
from marks.models import Mark
from attendance.forms import AttendanceForm
from attendance.models import Attendance
from account.models import Account
from student.models import Student
from account.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required(login_url="/login")
@allowed_users (allowed_roles=['student'])
def new_attendance_view(request):
    context = {}

    # form = AttendanceForm(request.POST)
    form = AttendanceForm()
    student_email = Account.objects.get(pk =request.user.id).email
    student_instance = Student.objects.get(institutional_email = student_email)
    form.fields['student'].initial = student_instance
    form.fields['student'].widget = forms.HiddenInput()
    context['form'] = form
    return render(request, 'attendance/attend.html', context)
@login_required(login_url="/login")
@allowed_users (allowed_roles=['student'])
def create_new_attendance(request):
     form = AttendanceForm(request.POST)
     if form.is_valid():
        student_instance = form.cleaned_data.get('student')
        course_instance = form.cleaned_data.get('course')
        try:
           Attendance.objects.get(student_id= student_instance.id,
            course_id = course_instance.id)
        except Attendance.DoesNotExist:
            new_attendance = Attendance(student = student_instance, course= course_instance)
            new_attendance.save()
            new_attendace_id = Attendance.objects.get(student = student_instance,
             course= course_instance).id
            new_mark = Mark(student_id=student_instance.id,course_id=course_instance.id,attendance_id=new_attendace_id)
            new_mark.save()
        else:
           messages.error(request, "Sorry but you are alerady attending this course")
        #    raise forms.ValidationError('You are already attending this course')
            
     return redirect('show', pk=request.user.id)
   #   return render(request,'attendance/attend.html')
