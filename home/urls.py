from django.urls import path
from . import views
from account.views import login_view
# app_name = 'personal'
urlpatterns = [
    path('', login_view),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('add_question/', views.add_question, name='add-question')
]