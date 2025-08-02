from django.contrib import admin
from .models import Seat

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['seat_id', 'status', 'reserved_until', 'last_updated']
    list_filter = ['status']
    search_fields = ['seat_id']