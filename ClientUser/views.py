from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from .models import*
from .serializers import*
from .serializers import*
from rest_framework.views import APIView
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
csrf_exempt
# Create your views here.

class ClientSignup(APIView):
     def post(self,request):
        try:
            postdata = SignupClient(data=request.data)
            print("--------------------")   
            print(request.data)
            print("--------------------")

            if postdata.is_valid():
                postdata.save()
            context = {
            'sucess': True,
            'status' : status.HTTP_200_OK,
            'response': postdata.data
                        }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)

class ClientLogin(APIView):
    def post(self,request):
        print("--------------------")
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            myuser = authenticate(username=username,password=password)
            if myuser:
                login(request,myuser)
            context = {
            'sucess': True,
            'status' : status.HTTP_200_OK,
            'response': 'login sucessfully'
                        }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
        
class ShowFiles(APIView):
    def get(self,request):
        try:
            showdata = OpsUser.objects.all()
            print("--------------")
            for i in showdata:
                print(i.uploaded_by)
                print(i.file_upload)
                print(i.id)

            serializer = ShowFilesSerializers(showdata, many =True)
            context = {
                'sucess': True,
                'status' : status.HTTP_200_OK,
                'response': serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)