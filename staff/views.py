from django.shortcuts import render


from rest_framework.views import APIView 
from rest_framework.response import Response

from staff.models import Doctor


class DoctorListCreateView(APIView):
    def get(self,request):
        qs = Doctor.objects.all().values()
        doctor_list = list(qs)
        return Response(data=doctor_list)

    def post(self,request):
        form_data = request.data
        Doctor.objects.create(**form_data)
        return Response(data={"Message":"Doctor Entered ......"})
    

class DoctorRetriveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs = Doctor.objects.filter(id=pk).values()
        doctorr_list = list(qs)
        return Response(data=doctorr_list)

    def put(self,request,pk=None):
        form_data = request.data
        Doctor.objects.filter(id=pk).update(**form_data)
        return Response(data={"Message":"Updated ..."})

    def delete(self,request,pk=None):
        Doctor.objects.get(id=pk).delete()
        return Response(data={"Message":"Deleted...."})