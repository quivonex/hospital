from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Feedback
from .serializers import FeedbackSerializer


# Create Feedback
class FeedbackCreateView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feedback submitted successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Update Feedback
class FeedbackUpdateView(APIView):
    def post(self, request):
        feedback_id = request.data.get("id")   # ID passed in body
        try:
            feedback = Feedback.objects.get(id=feedback_id)
        except Feedback.DoesNotExist:
            return Response({"error": "Feedback record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedbackSerializer(feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Feedback updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve Single Feedback
class FeedbackRetrieveView(APIView):
    def post(self, request):
        feedback_id = request.data.get("id")   # ID passed in body
        try:
            feedback = Feedback.objects.get(id=feedback_id)
        except Feedback.DoesNotExist:
            return Response({"error": "Feedback record not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FeedbackSerializer(feedback)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


# Retrieve All Feedback
class FeedbackListView(APIView):
    def post(self, request):
        feedbacks = Feedback.objects.all().order_by("-created_at")
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
