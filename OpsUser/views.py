
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

class OpsUploadFiles(APIView):
    def post(self,request):
        try:
            # uploaded_by = request.POST['uploaded_by']
            # file_upload = request.POST['file_upload']
            # a = OpsUser(uploaded_by=uploaded_by,file_upload=file_upload)
            # print(a)
            # a.save()
            # print("00000000000000000000000000000000")
            # print("---------------------------")
            # print(User)
            all = OpsUser.objects.all()
            # print(all)
            for i in all:
                print(i.uploaded_by)
                print(i.file_upload)
            # print("==============================")
            # print(request.data)
            # print("==============================")
            # for i in request.data:
            #     print(i.file_upload)
            #     print(i.uploaded_by)
            # if request.method == 'POST':
            #     uploaded_by =  request.POST['admin']
            #     file_upload = request.POST['Paramjeet_Singh_Cv (1).pdf (application/pdf)']
            #     a = OpsUser(uploaded_by=uploaded_by,file_upload=file_upload)
            #     a.save()
            #     print("............................")
            #     print(a)
            #     print("............................")
            # print(postdata)
            postdata = SerializersFileData(data = request.data)
            if postdata.is_valid():
                postdata.save()
                # files = postdata.validated_data['file_upload','uploaded_by']
                # files.save()
                print('...............')
                # print(files)
                print('...............')

                # uploaded_file = postdata.validated_data['uploaded_by']
                # uploaded_file.save()
            context = {
                'sucess': True,
                'status' : status.HTTP_200_OK,
                'response': 'file upload sucesssfully'
            }
            return Response(context,status=status.HTTP_200_OK)
        except Exception as E:
            context = {
                'sucess': False,
                'status' : status.HTTP_400_BAD_REQUEST,
                'response': str(E)
                }
            return Response(context,status.HTTP_400_BAD_REQUEST)
        
class OpsSignUp(APIView):
     

    def post(self,request):
        try: 
            postdata = SignupOps(data=request.data)
            print("--------------------")   
            print(request.data)
            print("--------------------")
            print(postdata)
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

class OpsLogin(APIView):
    def post(self,request):
        print("--------------------")
        try:
            username = request.data.get('username')
            print(username)
            password = request.data.get('password')
            print(password)
            myuser = authenticate(username=username,password=password)
            print("+++++++++++++++++++++++++")
            print(myuser)
            if myuser is not None:
                login(request,myuser)
                print("----@@@@@@@@@@-----")
                print(myuser)
                print("---------------") 
            else:
                return Response('invalid creadentials')
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
            

