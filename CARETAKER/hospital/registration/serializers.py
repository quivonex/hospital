from rest_framework import serializers
from .models import Register, CustomerProfile, AdminProfile, DoctorProfile, CaretakerProfile


# -----------------------
# Register Serializer
# -----------------------
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # hide password from GET response
        }

    def create(self, validated_data):
        user = Register(**validated_data)
        user.set_password(validated_data['password'])  # hash password
        user.save()
        return user


# -----------------------
# Customer Serializer
# -----------------------
class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProfile
        fields = '__all__'


# -----------------------
# Admin Serializer
# -----------------------
class AdminProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProfile
        fields = '__all__'


# -----------------------
# Doctor Serializer
# -----------------------
class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'


# -----------------------
# Caretaker Serializer
# -----------------------
class CaretakerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaretakerProfile
        fields ='__all__'
