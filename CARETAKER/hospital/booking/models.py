from django.db import models
from django.utils import timezone
from registration.models import CaretakerProfile   # adjust app name if needed
from registration.models import CustomerProfile

class CaretakerBooking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name="bookings")
    caretaker = models.ForeignKey(CaretakerProfile, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(default=timezone.now)   # when the booking was made
    session_date = models.DateField()                          # actual date of caretaker session
    session_time = models.TimeField()                          # session start time
    duration = models.PositiveIntegerField(help_text="Duration in hours")  # session duration
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)            # optional customer notes

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} - {self.customer} with {self.caretaker} on {self.session_date}"
