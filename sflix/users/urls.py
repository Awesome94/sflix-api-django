from django.urls import path
from .views import ListUsersView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all")
]
