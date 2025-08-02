from rest_framework import viewsets
from .models import Seat
from .serializers import SeatSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer