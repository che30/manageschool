from multiprocessing import context
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.models import Account
from django.urls import reverse
from account.forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from marks.models import Mark
from student.models import Student
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from attendance.models import Attendance
import datetime
@unauthenticated_user
def register_view(request, *args, **kwargs):
	# user = request.user
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user=form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			group = Group.objects.get(name = 'student')
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			# print(user)
			group.user_set.add(user)
			# user.group.add(group)
			return redirect('show', pk=request.user.id)
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)
@login_required(login_url="login")
# @allowed_users(allowed_roles=['student'])
def show_view(request, pk):
	context = {}
	current_date = datetime.datetime.now()
	attendance = None
	course_marks = None
	try:
		Account.objects.get(pk = pk)
		user = Student.objects.get(institutional_email = request.user.email)
		attendance = Attendance.objects.filter(student_id = user.id,
		date__contains= str(current_date)[:4])
		course_marks =  Mark.objects.filter(student_id = user.id).filter(attendance__date__contains = str(current_date)[:4])
	except Account.DoesNotExist:
		return render(request,'404.html')
	if request.user.id != pk:
		return render(request,'404.html')
	context['attendance'] = attendance
	context['course_marks'] = course_marks
	return render(request, 'account/show.html',context)

def logout_view(request):
	logout(request)
	return redirect("login")
@unauthenticated_user
def login_view(request, *args, **kwargs):
	context = {}
	user = request.user

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
			if request.user.is_staff and request.user.is_admin == False:
				return redirect('my-courses')
			elif request.user.is_staff==False and request.user.is_admin == False:
				return redirect('show',pk=request.user.id)
			else:
				return redirect('transcripts')

	else:
		form = LoginForm()

	context['login_form'] = form

	return render(request, "account/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect
@login_required(login_url="login")
# @allowed_users(allowed_roles=['admin'])
def transcript_view(request):
	current_date = datetime.datetime.now()
	id = None
	context = {}
	if request.POST:
		mat_num = request.POST.get('matricule')
		try:
			id = Student.objects.get(matricule_number = mat_num).id
			mark =  Mark.objects.filter(student_id = id)
			print(mark)
			context['marks'] = mark
		except Student.DoesNotExist:
			return render(request,'404.html')
	return render(request, "account/transcript.html",context)