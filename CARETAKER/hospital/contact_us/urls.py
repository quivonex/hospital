from django.urls import path
from .views import (
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsRetrieveView,
    ContactUsListView,
)

urlpatterns = [
    path("contact/create/", ContactUsCreateView.as_view(), name="contact-create"),
    path("contact/update/", ContactUsUpdateView.as_view(), name="contact-update"),
    path("contact/retrieve/", ContactUsRetrieveView.as_view(), name="contact-retrieve"),
    path("contact/list/", ContactUsListView.as_view(), name="contact-list"),
]
