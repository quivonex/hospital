from django.urls import path
from .views import (
    FeedbackCreateView,
    FeedbackUpdateView,
    FeedbackRetrieveView,
    FeedbackListView,
)

urlpatterns = [
    path("feedback/create/", FeedbackCreateView.as_view(), name="feedback-create"),
    path("feedback/update/", FeedbackUpdateView.as_view(), name="feedback-update"),
    path("feedback/retrieve/", FeedbackRetrieveView.as_view(), name="feedback-retrieve"),
    path("feedback/list/", FeedbackListView.as_view(), name="feedback-list"),
]
