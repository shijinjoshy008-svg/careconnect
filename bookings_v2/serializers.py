
from rest_framework import serializers

# class SignUPSerializers(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.CharField()
#     password = serializers.CharField()

from django.contrib.auth.models import User
from bookings.models import Appointment
from datetime import datetime

class SignUpSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username","email","password"]

class AppoinmentSerializer(serializers.ModelSerializer):
    doctor=serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = "__all__"
        read_only_fields = ["id","token_number","appointment_time","created_at"]
    def validate(self, validated_date):
        appointment_date=validated_date.get("appointment_date")
        doctor= validated_date.get("doctor")
        if appointment_date <datetime.today().date():
            raise serializers.ValidationError("date should be > cur date")
        last_appointment_object=Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()
        if last_appointment_object:
            if last_appointment_object.token_number==25:
                raise serializers.ValidationError("slot full...")
            return validated_date
        