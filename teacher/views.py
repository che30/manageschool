from django.shortcuts import render,redirect
from attendance.models import Attendance
from courses.models import Course
from django.forms import modelformset_factory
# from marks.forms import UpdateMarkForm
from marks.models import Mark
import datetime

from teacher.forms import UpdateMarksForm
# Create your views here.
def show_teacher_view(request):
    context = {}
    teacher_course = Course.objects.filter(teacher__institutional_email =request.user.email)
    context['teacher_course'] = teacher_course
    return render(request, 'teacher/show.html',context)
def render_update_marks_marks(request, course_id):
    context = {}
    student_marks = []
    current_date = datetime.datetime.now()
    attendance_date_arr = []
    attendance_dates = Attendance.objects.filter(course_id=course_id,
    date__contains=str(current_date)[:4])
    for attendance_date in attendance_dates:
        attendance_date_arr.append(attendance_date.id)
        # attendace_ids.append(attendance_date.id)
        # if str(attendance_date.date)[:-6] == str(current_date)[:4]:
        student_marks.append(Mark.objects.get(attendance_id=attendance_date.id,
course_id=course_id))
    # print("before test")
    # print(attendance_date_arr)
    # print("after test")
    markFormSet = modelformset_factory(Mark, fields = ['ca_one'])
    form = markFormSet(queryset=Mark.objects.filter(attendance_id__in = attendance_date_arr))
    if request.POST:
        for index, mark in enumerate(student_marks):
            mark.ca_one = int(request.POST.get(f"form-{index}-ca_one"))
            mark.save()
            # Mark.objects.get(pk = mark.id).update(ca_one = int(request.POST.get(f"form-{index}-ca_one")) )
            # mark.update(ca_one = int(request.POST.get(f"form-{index}-ca_one")))
            # print(request.POST.get(f"form-{index}-ca_one"))
        # for instance in editedForm:
        #     print(instance)
        return redirect('my-courses')
#             student_marks = Mark.objects.filter(attendance_id=attendance_date.id,
# course_id=course_id)
    context['student_marks'] = student_marks
    context['form'] = form
    context['course_id'] = course_id
    return render(request, 'teacher/display_marks.html',context)
def update_marks(request):
    # print(request.POST)
    if request.POST:
        # form = UpdateMarksForm(request.POST)
        # if form.is_valid():
        print(" c'est belle et bien la")
        print(" c'est belle et bien la")
    else:
        form = UpdateMarksForm()
        # context['form'] = form
    return redirect('my-courses')