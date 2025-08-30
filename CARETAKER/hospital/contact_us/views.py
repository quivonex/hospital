from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs
from .serializers import ContactUsSerializer

# Create Contact Message
class ContactUsCreateView(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact query submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Contact Message
class ContactUsUpdateView(APIView):
    def post(self, request):
        contact_id = request.data.get("id")   # ID passed in body instead of pk in URL
        try:
            contact = ContactUs.objects.get(id=contact_id)
        except ContactUs.DoesNotExist:
            return Response({"error": "Contact record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact query updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve Single Contact Message
class ContactUsRetrieveView(APIView):
    def post(self, request):
        contact_id = request.data.get("id")   # ID passed in body
        try:
            contact = ContactUs.objects.get(id=contact_id)
        except ContactUs.DoesNotExist:
            return Response({"error": "Contact record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


# Retrieve All Contact Messages
class ContactUsListView(APIView):
    def post(self, request):
        contacts = ContactUs.objects.all().order_by("-created_at")
        serializer = ContactUsSerializer(contacts, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
