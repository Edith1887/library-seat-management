import os, sys, django
sys.path.append("D:/library-seat-management")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "libraryapp.settings")
django.setup()

from seatmanager.models import Seat

# Add or print seats
Seat.objects.create(seat_id="A1", status="green")
for seat in Seat.objects.all():
    print(seat.seat_id, seat.status)