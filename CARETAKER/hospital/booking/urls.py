from django.urls import path
from .views import (
    CreateBookingView,
    UpdateBookingView,
    RetrieveBookingView,
    ListBookingView,
)

urlpatterns = [
    path("booking/create/", CreateBookingView.as_view(), name="create-booking"),
    path("booking/update/", UpdateBookingView.as_view(), name="update-booking"),
    path("booking/retrieve/", RetrieveBookingView.as_view(), name="retrieve-booking"),
    path("booking/list/", ListBookingView.as_view(), name="list-bookings"),
]
