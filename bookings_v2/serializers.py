
from rest_framework import serializers

# class SignUPSerializers(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.CharField()
#     password = serializers.CharField()

from django.contrib.auth.models import User
from bookings.models import Appointment

class SignUpSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email","password"]

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["id","token_number","appointment_time","created_at"]