from django.shortcuts import render, get_object_or_404, redirect
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
