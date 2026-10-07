from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from bookings_v2.serializers import SignUpSerializers,AppoinmentSerializer

from bookings.models import Appointment

from datetime import time,datetime,timedelta



# Create your views here.

class SignUpView(APIView):
    def post(self,request):
        form_data = request.data
        serializer_instance = SignUpSerializers(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            user_object = User.objects.create_user(**cleaned_data)
            
            serializer_instance = SignUpSerializers(user_object)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class AppoinmentListCreateView(APIView):
    def get(self,request):
        qs = Appointment.objects.all()
        serializer_instacne = AppoinmentSerializer(qs,many=True)
        return Response(data=serializer_instacne.data)

    def post(self,request):
        form_data = request.data
        serializer_instance = AppoinmentSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data

            doctor_id = cleaned_data.get("doctor")
            appointment_date = cleaned_data.get("appointment_date")

            new_token = 0
            last_appointment_object = Appointment.objects.filter(doctor=doctor_id,appointment_date=appointment_date).last()
            appoinment_time = time(10,0)

            if last_appointment_object:
                cleaned_data["token_number"] = last_appointment_object.token_number+1

                #appoinment date setting
                next_appointment_date_time = datetime.combine(appointment_date,last_appointment_object.appointment_time)+timedelta(minutes=15)
                appoinment_time = next_appointment_date_time.time()



            else:
                cleaned_data["token_number"] = 1

            qs = Appointment.objects.create(**cleaned_data,appointment_time=appoinment_time)
            serializer_instance = AppoinmentSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)