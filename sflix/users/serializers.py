from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("firstname", "last_name")

class TokenSerializer(serializers.Serializer):
    """
    This will serialize the token data
    """
    token  = serializers.CharField(max_length=255)
