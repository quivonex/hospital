from rest_framework import serializers
from .models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'   # includes all fields from model
        read_only_fields = ['created_at', 'updated_at']
