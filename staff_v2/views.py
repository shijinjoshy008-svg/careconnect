from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class DoctorListCreateV2(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        qs = Doctor.objects.all()
        serializer_instacne = DoctorSerializer(qs,many=True)
        return Response(data=serializer_instacne.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = DoctorSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.data
            Doctor.objects.create(**cleaned_data)
            return Response(data=cleaned_data)

        else:
            return Response(data=serializer_instance.errors)

class DoctorFilterDeleteUpdateView(APIView):
    def delete(self,reuest,pk=None):
        Doctor.objects.filter(id=pk).delete()
        return Response({"Message":""})

    def get(self,request,pk=None):
        qs = Doctor.objects.filter(id=pk)
        serializer_instance = DoctorSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data = request.data
        serializer_instace = DoctorSerializer(data=form_data)
        if serializer_instace.is_valid():
            cleaned_data = serializer_instace.validated_data
            Doctor.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=cleaned_data)
        else:
            return Response(data=serializer_instace.errors)

class AdminCreateView(APIView):
    def post(self,request,pk=None):
        form_data = request.data
        serializer_instance = UserSerializer(data = form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            #User.objects.create_superuser(**cleaned_data)
            User.objects.create(**cleaned_data)
            #User.objects.create_user(**cleaned_data)
            return Response(data= serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

    def get(self,request):
        qs = User.objects.all()
        serializer_instacne = UserSerializer(qs,many=True)
        return Response(data=serializer_instacne.data)


