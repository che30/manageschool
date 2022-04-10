from django.shortcuts import render
# Create your views here.
# app_name = 'home'
def home_screen_view(request):
  context = {}
  return render(request, 'home/home.html',context)