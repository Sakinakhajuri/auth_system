from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Register
from .serializers import RegisterSerializer,LoginSerializer
from rest_framework.response import Response

# Create your views here.

class listView (APIView):
    def post(self, request,*args,**kwargs):
        print(request.data)
        serializer= RegisterSerializer(data=request.data)
        #print(request.body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"error":None,"message":"Successfully registered"})
        return JsonResponse({"error":"User already exists","message":None})

class loginView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        print(serializer.is_valid())
        print("serializer data : ",serializer.data)
        print("request data : ",request.data)
        if serializer.is_valid():
            print(serializer.data)
            user = Register.objects.filter(email=serializer.data["email"])
            if(len(user) != 0):
                print(user)
                if(user[0].password==serializer.data["password"]):
                    return JsonResponse({"error":None,"message":"logged in successfully"})
                else:
                    return JsonResponse({"error":"username/password incorrect","message":None})
            else:
                return JsonResponse({"error": "user does not exist","message":None})
        return JsonResponse({"error":"please provide proper parameters","message":None})
