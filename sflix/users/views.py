from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions

from .models import Users
from .serializers import UsersSerializer
from rest_framework import generics
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
