from django.urls import path
from .views import ListUsersView, LoginView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name="users-all"),
    path('auth/login', LoginView.as_view(), name="login"),
    path('auth/register', RegisterView.as_view(), name="register")
]
