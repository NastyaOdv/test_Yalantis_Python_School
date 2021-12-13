from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet
router = DefaultRouter()
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
urlpatterns = router.urls