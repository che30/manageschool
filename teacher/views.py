from django.shortcuts import render
from courses.models import Course
import teacher
# Create your views here.
def show_teacher_view(request):
    context = {}
    teacher_course = Course.objects.filter(teacher__institutional_email =request.user.email)
    context['teacher_course'] = teacher_course
    return render(request, 'teacher/show.html',context)
def update_marks(request, course_id):
    context = {}
    return render(request, 'teacher/update_marks.html',context)