from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'properties', PropertyViewSet, basename='listing')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls
