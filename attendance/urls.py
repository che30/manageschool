from django.urls import path
from . import views
# app_name = 'account'
urlpatterns = [
    path('new-attendance/', views.new_attendance_view,name='new-attendance'),
    path('create-attedance/',views.create_new_attendance,name="create-attendance"),
    # path('show',views.show_view, name='show'),
 
]