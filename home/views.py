from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.decorators import unauthenticated_user,allowed_users
# Create your views here.
# app_name = 'home'
@login_required
@unauthenticated_user
@allowed_users(allowed_roles=['admin'])
def home_screen_view(request):
  context = {}
  return render(request, 'home/home.html',context)