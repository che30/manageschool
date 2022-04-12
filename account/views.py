from django.shortcuts import render
from django.http import Http404
from django import forms
from attendance.forms import AttendanceForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.models import Account
from django.urls import reverse
from account.forms import RegistrationForm, LoginForm
from student.models import Student
from courses.models import Course


def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return redirect('show',pk=request.user.id)

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('show', pk=request.user.id)
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)
def show_view(request, pk):
	context = {}
	form = AttendanceForm()
	if request.user.is_authenticated == False:
		return redirect('login')
	try:
		Account.objects.get(pk = pk)
	except Account.DoesNotExist:
		return render(request,'404.html')
	
	# if student_number != 'adminone':
	# 	student_instance = Student.objects.filter(registration_number = student_number)[0]
		# form.fields['student'].initial = student_instance
	# else:
		# return redirect("show-admin")
	# form.fields['student'].widget = forms.HiddenInput()
	# context['form'] = form
	return render(request, 'account/show.html',context)

def logout_view(request):
	logout(request)
	return redirect("login")


def login_view(request, *args, **kwargs):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('show',pk=request.user.id)

	destination = get_redirect_if_exists(request)
	# print("destination: " + str(destination))

	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				if destination:
					return redirect(destination)
				# user = Account.objects(pk = request.user.id)
				# return redirect('show')
				if user.is_staff:
					return redirect('my-courses')
					# redirect(reverse('my-course', kwargs={ 'courses': teacher_course }))
				return redirect("show", pk=request.user.id)

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
def admins_only_view(request):
	return HttpResponse(request, "admin/")
