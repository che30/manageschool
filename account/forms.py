from django import forms
from student.models import Student
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
	registration_number = forms.CharField(min_length=8)
	class Meta:
		model = Account
		fields = ('email', 'username', 'password1', 'password2','registration_number' )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
	def clean_registration_number(self):
		registration_number = self.cleaned_data['registration_number']
		print(registration_number)
		try:
			Student.objects.get(registration_number = registration_number)
		except Student.DoesNotExist:
			raise forms.ValidationError('Registration number"%s" is invalid.' % registration_number)
		else:
			return registration_number
class LoginForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	class Meta:
		model = Account
		fields = ('email', 'password')
	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")
