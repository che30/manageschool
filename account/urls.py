from django.urls import path
from . import views
# app_name = 'account'
urlpatterns = [
    path('users/<int:pk>',views.show_view, name='show'),
    path('Register/', views.register_view, name='register'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    # path('show',views.show_view, name='show'),
 
]