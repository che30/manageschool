from multiprocessing import context
from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.models import Account

from account.forms import RegistrationForm, LoginForm


def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

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
			return redirect('show')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)
def show_view(request, pk):
	context =  {}
	account = None
	if request.user.is_authenticated == False:
		return redirect('login')
	try:
		account = Account.objects.get(pk = pk)
	except Account.DoesNotExist:
		return render(request,'404.html')
	print (account)
	
	# print("before pk ")
	# print(pk)
	return render(request, 'account/show.html',{})

def logout_view(request):
	logout(request)
	return redirect("login")


def login_view(request, *args, **kwargs):
	context = {}
	user = request.user
	if user.is_authenticated:
		return redirect('show')

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
