from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.all_users, name='all_users')
]
