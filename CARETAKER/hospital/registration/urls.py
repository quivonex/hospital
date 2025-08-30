from django.urls import path
from .views import (
    RegisterCreateView,
    RegisterUpdateView,
    RegisterRetrieveByIdView,
    RegisterRetrieveAllView,
    LoginView,

    CustomerProfileCreateView,
    CustomerProfileUpdateView,
    CustomerProfileRetrieveView,
    CustomerProfileRetrieveAllView,

    AdminProfileCreateView,
    AdminProfileUpdateView,
    AdminProfileRetrieveView,
    AdminProfileRetrieveAllView,

    DoctorProfileCreateView,
    DoctorProfileUpdateView,
    DoctorProfileRetrieveView,
    DoctorProfileRetrieveAllView,

    CaretakerProfileCreateView,
    CaretakerProfileUpdateView,
    CaretakerProfileRetrieveView,
    CaretakerProfileRetrieveAllView,
)

urlpatterns = [
    path('register/create/', RegisterCreateView.as_view(), name='register-create'),
    path('register/update/', RegisterUpdateView.as_view(), name='register-update'),
    path('register/retrive-by-id/', RegisterRetrieveByIdView.as_view(), name='register-retrieve-by-id'),
    path('register/all/', RegisterRetrieveAllView.as_view(), name='register-all'),
    path("login/admin/", LoginView.as_view(), name="login-admin"),

    path("customer/create/", CustomerProfileCreateView.as_view(), name="customer-create"),
    path("customer/update/", CustomerProfileUpdateView.as_view(), name="customer-update"),
    path("customer/retrieve/", CustomerProfileRetrieveView.as_view(), name="customer-retrieve"),
    path("customer/retrieve-all/", CustomerProfileRetrieveAllView.as_view(), name="customer-retrieve-all"),

    path("admin/create/", AdminProfileCreateView.as_view(), name="admin-create"),
    path("admin/update/", AdminProfileUpdateView.as_view(), name="admin-update"),
    path("admin/retrieve/", AdminProfileRetrieveView.as_view(), name="admin-retrieve"),
    path("admin/retrieve-all/", AdminProfileRetrieveAllView.as_view(), name="admin-retrieve-all"),

    path("doctor/create/", DoctorProfileCreateView.as_view(), name="doctor-create"),
    path("doctor/update/", DoctorProfileUpdateView.as_view(), name="doctor-update"),
    path("doctor/retrieve/", DoctorProfileRetrieveView.as_view(), name="doctor-retrieve"),
    path("doctor/retrieve-all/", DoctorProfileRetrieveAllView.as_view(), name="doctor-retrieve-all"),

    path("caretaker/create/", CaretakerProfileCreateView.as_view(), name="caretaker-create"),
    path("caretaker/update/", CaretakerProfileUpdateView.as_view(), name="caretaker-update"),
    path("caretaker/retrieve/", CaretakerProfileRetrieveView.as_view(), name="caretaker-retrieve"),
    path("caretaker/retrieve-all/", CaretakerProfileRetrieveAllView.as_view(), name="caretaker-retrieve-all"),


]
