from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CaretakerBooking
from .serializers import CaretakerBookingSerializer


# CREATE BOOKING
class CreateBookingView(APIView):
    def post(self, request):
        serializer = CaretakerBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Booking created successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# UPDATE BOOKING
class UpdateBookingView(APIView):
    def post(self, request):
        booking_id = request.data.get("id")
        if not booking_id:
            return Response({"error": "Booking ID is required for update."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = CaretakerBooking.objects.get(id=booking_id)
        except CaretakerBooking.DoesNotExist:
            return Response({"error": "Booking not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CaretakerBookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Booking updated successfully", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# RETRIEVE SINGLE BOOKING
class RetrieveBookingView(APIView):
    def post(self, request):
        booking_id = request.data.get("id")
        if not booking_id:
            return Response({"error": "Booking ID is required to retrieve."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            booking = CaretakerBooking.objects.get(id=booking_id)
        except CaretakerBooking.DoesNotExist:
            return Response({"error": "Booking not found."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = CaretakerBookingSerializer(booking)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


# RETRIEVE ALL BOOKINGS
class ListBookingView(APIView):
    def post(self, request):
        bookings = CaretakerBooking.objects.all()
        serializer = CaretakerBookingSerializer(bookings, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
