from django.urls import path
from . import views
# app_name = 'account'
urlpatterns = [
    path('my-courses/',views.show_teacher_view, name='my-courses'),
    path('my-courses/<int:course_id>/<int:id>/',views.render_update_marks,name='show-marks'),
    path('update-marks',views.update_marks,name='update-marks'),
    # path('Register/', views.register_view, name='register'),
    # path('login/',views.login_view, name='login'),
    # path('logout/',views.logout_view, name='logout'),
    # path('admins-only',views.admins_only_view, name="show-admin")
    # path('show',views.show_view, name='show'),
 
]