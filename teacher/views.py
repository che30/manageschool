from django.shortcuts import render,redirect
from attendance.models import Attendance
from courses.models import Course
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from account.decorators import allowed_users
# from marks.forms import UpdateMarkForm
from marks.models import Mark
import datetime
# Create your views here.
@login_required(login_url="/login")
@allowed_users(allowed_roles=['staff'])
def show_teacher_view(request):
    context = {}
    teacher_course = Course.objects.filter(teacher__institutional_email =request.user.email)
    context['teacher_course'] = teacher_course
    return render(request, 'teacher/show.html',context)
@login_required(login_url="/login")
def render_update_marks(request,course_id, id=None):
   exam_type = None
   if id == 1:
       exam_type = 'ca'
   elif id == 2:
       exam_type = 'exam'
   else:
       exam_type = 'resit'
   if  request.user.is_authenticated == False:
       return redirect('login')
   context = {}
   context['course_name'] = Course.objects.get(pk=course_id).name
   student_marks = []
   current_date = datetime.datetime.now()
   attendance_date_arr = []
   attendance_dates = Attendance.objects.filter(course_id=course_id,
   date__contains=str(current_date)[:4])
   for attendance_date in attendance_dates:
       attendance_date_arr.append(attendance_date.id)
       student_marks.append(Mark.objects.get(attendance_id=attendance_date.id,
course_id=course_id))
       markFormSet = modelformset_factory(Mark, fields = [f"{exam_type}"])
       form = markFormSet(queryset=Mark.objects.filter(attendance_id__in = attendance_date_arr))
   if request.POST:
        for index, mark in enumerate(student_marks):
            if exam_type == 'ca':
                mark.ca = int(request.POST.get(f"form-{index}-{exam_type}"))
            elif exam_type == 'exam':
                mark.exam = int(request.POST.get(f"form-{index}-{exam_type}"))
                mark.total = mark.ca + mark.exam
            else:
                mark.resit = int(request.POST.get(f"form-{index}-{exam_type}"))
                mark.total = mark.ca + mark.resit
            # mark.exam_type = int(request.POST.get(f"form-{index}-{exam_type}"))
            mark.save()
        all_marks = Mark.objects.all()
        for mark in all_marks:
            if mark.total >=80 and mark.total <=100:
                mark.grade = 'A'
            elif mark.total >=60 and mark.total<=79:
                mark.grade = 'B'
            elif mark.total >=50 and mark.total<=59:
                mark.grade = 'C'
            elif mark.total >=40 and mark.total<=49:
                mark.grade = 'D'
            else:
                mark.grade = 'F'
            mark.save()
        return redirect('my-courses')
   if id ==1:
       context['exam'] = 'Continous Assesment'
   elif id ==2:
       context['exam'] = 'EXAM'
   else:
       context['exam'] = 'RESIT'
   context['student_marks'] = student_marks
   context['form'] = form
   context['course_id'] = course_id
   context['id'] = id
   return render(request, 'teacher/display_marks.html',context)
def update_marks(request):
    return redirect('my-courses')