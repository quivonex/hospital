from django.db import models
from registration.models import CaretakerProfile   # adjust app name if needed
from registration.models import CustomerProfile     # adjust app name if needed

class Feedback(models.Model):
    caretaker = models.ForeignKey(CaretakerProfile, on_delete=models.CASCADE, related_name="feedbacks")
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name="given_feedbacks")
    rating = models.PositiveIntegerField(default=1)  # 1 to 5 stars
    comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)  # when query submitted

    def __str__(self):
        return f"Feedback by {self.customer.id} for {self.caretaker.id} - {self.rating}⭐"
