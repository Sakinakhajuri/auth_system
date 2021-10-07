from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model=Register
       fields=['name','email','password']

class LoginSerializer(serializers.Serializer):
       email=serializers.EmailField(max_length=100)
       password=serializers.CharField(max_length=100)

