


from rest_framework import serializers
from staff.models import Doctor
# Create your models here.

class DoctorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    specialization = serializers.ChoiceField(choices = Doctor.SPECIALIZATION_OPTIONS)
    fee = serializers.IntegerField()
    qualification = serializers.CharField()
    email = serializers.CharField()

    def __str__(self):
        return self.name

    def validate(self,validated_data):
        fee = validated_data.get("fee")
        if fee < 0 :
            raise serializers.ValidationError("Fee should be greated than 0")
        return validated_data

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()