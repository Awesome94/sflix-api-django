from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions

from .models import Users
from .serializers import UsersSerializer
from rest_framework import generics

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your views here.

class ListUsersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    permissions_classes = (permissions.AllowAny)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username  = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            serializer = TokenSerializer(data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )})
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNATHORIZED)

class RegisterView(generics.CreateAPIView):
    """
    POST 'auth/register/'
    """
    permissions_class = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data,get("email", "")
        if not username  and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is required to register a user"
                }
            )
        new_user = Users(username=username, password=password, email=email)
        return Response(status=status.HTTP_201_CREATED)
