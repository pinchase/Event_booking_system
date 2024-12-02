# Step 3: Create models in booking/models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Price field
    description = models.TextField()

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Link to Event
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    number_of_tickets = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)  # When the booking was made

    def __str__(self):
        return f"{self.user_name} - {self.event.title} - {self.number_of_tickets} tickets"
