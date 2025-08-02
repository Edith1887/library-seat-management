from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from seatmanager.views import SeatViewSet

router = routers.DefaultRouter()
router.register(r'seats', SeatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
