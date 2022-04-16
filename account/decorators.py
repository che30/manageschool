from django.http import HttpResponse
from django.shortcuts import redirect
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff and request.user.is_admin == False:
                return redirect('my-courses')
            elif request.user.is_staff==False and request.user.is_admin == False:
                return redirect('show',pk=request.user.id)
            else:
                return redirect('transcripts')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func
def allowed_users(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return  HttpResponse('YOU ARE NOT AUTHORIZED TO VIEW THIS PAGE')
        return wrapper_func
    return decorator