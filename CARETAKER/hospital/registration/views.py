from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Register
from .serializers import RegisterSerializer


class RegisterCreateView(APIView):
    """Create a new user"""
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class RegisterUpdateView(APIView):
    """Update user using ID from request body"""
    def post(self, request):
        user_id = request.data.get("id")
        if not user_id:
            return Response(
                {"error": "User ID is required for update"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = Register.objects.get(id=user_id)
        except Register.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RegisterSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"error": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class RegisterRetrieveByIdView(APIView):
    """Retrieve single user using ID from request body"""
    def post(self, request):
        user_id = request.data.get("id")
        if not user_id:
            return Response(
                {"error": "User ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = Register.objects.get(id=user_id)
        except Register.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = RegisterSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class RegisterRetrieveAllView(APIView):
    """Retrieve all users"""
    def post(self, request):
        users = Register.objects.all()
        if not users.exists():
            return Response(
                {"message": "No users found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = RegisterSerializer(users, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

#### login ###

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Register

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        role = request.data.get("role")

        if not username or not password or not role:
            return Response({"error": "Username, password, and role are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Register.objects.get(username=username, role=role)
        except Register.DoesNotExist:
            return Response({"error": "Invalid username or role."},
                            status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response({"error": "Invalid password."},
                            status=status.HTTP_401_UNAUTHORIZED)

        # Success Response
        return Response({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
        }, status=status.HTTP_200_OK)


################################################################################################################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomerProfile, Register
from .serializers import CustomerProfileSerializer


class CustomerProfileCreateView(APIView):
    def post(self, request):
        serializer = CustomerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Customer Profile created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomerProfileUpdateView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = CustomerProfile.objects.get(id=profile_id)
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Customer Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CustomerProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Customer Profile updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class CustomerProfileRetrieveView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = CustomerProfile.objects.get(id=profile_id)
            serializer = CustomerProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Customer Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class CustomerProfileRetrieveAllView(APIView):
    def post(self, request):
        profiles = CustomerProfile.objects.all()
        if not profiles.exists():
            return Response(
                {"success": False, "message": "No Customer Profiles found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CustomerProfileSerializer(profiles, many=True)
        return Response(
            {"success": True, "count": profiles.count(), "data": serializer.data},
            status=status.HTTP_200_OK
        )


######################################################################################################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import AdminProfile
from .serializers import AdminProfileSerializer


class AdminProfileCreateView(APIView):
    def post(self, request):
        serializer = AdminProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Admin Profile created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class AdminProfileUpdateView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = AdminProfile.objects.get(id=profile_id)
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Admin Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Admin Profile updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class AdminProfileRetrieveView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = AdminProfile.objects.get(id=profile_id)
            serializer = AdminProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Admin Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class AdminProfileRetrieveAllView(APIView):
    def post(self, request):
        profiles = AdminProfile.objects.all()
        if not profiles.exists():
            return Response(
                {"success": False, "message": "No Admin Profiles found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AdminProfileSerializer(profiles, many=True)
        return Response(
            {"success": True, "count": profiles.count(), "data": serializer.data},
            status=status.HTTP_200_OK
        )

###################################################################################################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer


class DoctorProfileCreateView(APIView):
    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Doctor Profile created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorProfileUpdateView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = DoctorProfile.objects.get(id=profile_id)
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Doctor Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DoctorProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Doctor Profile updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorProfileRetrieveView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = DoctorProfile.objects.get(id=profile_id)
            serializer = DoctorProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Doctor Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class DoctorProfileRetrieveAllView(APIView):
    def post(self, request):
        profiles = DoctorProfile.objects.all()
        if not profiles.exists():
            return Response(
                {"success": False, "message": "No Doctor Profiles found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = DoctorProfileSerializer(profiles, many=True)
        return Response(
            {"success": True, "count": profiles.count(), "data": serializer.data},
            status=status.HTTP_200_OK
        )

################################################################################################################

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import CaretakerProfile
from .serializers import CaretakerProfileSerializer


class CaretakerProfileCreateView(APIView):
    def post(self, request):
        serializer = CaretakerProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Caretaker Profile created successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class CaretakerProfileUpdateView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = CaretakerProfile.objects.get(id=profile_id)
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Caretaker Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CaretakerProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "message": "Caretaker Profile updated successfully", "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"success": False, "message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class CaretakerProfileRetrieveView(APIView):
    def post(self, request):
        profile_id = request.data.get("id")
        if not profile_id:
            return Response(
                {"success": False, "message": "Profile ID is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            profile = CaretakerProfile.objects.get(id=profile_id)
            serializer = CaretakerProfileSerializer(profile)
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        except ObjectDoesNotExist:
            return Response(
                {"success": False, "message": "Caretaker Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )


class CaretakerProfileRetrieveAllView(APIView):
    def post(self, request):
        profiles = CaretakerProfile.objects.all()
        if not profiles.exists():
            return Response(
                {"success": False, "message": "No Caretaker Profiles found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CaretakerProfileSerializer(profiles, many=True)
        return Response(
            {"success": True, "count": profiles.count(), "data": serializer.data},
            status=status.HTTP_200_OK
        )
