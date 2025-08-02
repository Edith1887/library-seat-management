from django.db import models
from django.utils import timezone

class Seat(models.Model):
    STATUS_CHOICES = [
        ('green', 'Available'),
        ('yellow', 'Reserved'),
        ('red', 'Occupied')
    ]

    seat_id = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='green')
    reserved_until = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.seat_id} - {self.status}"