from rest_framework import serializers
from .models import CaretakerBooking

class CaretakerBookingSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = CaretakerBooking
        fields = '__all__'
        read_only_fields = ["id", "booking_date", "created_at", "updated_at"]
