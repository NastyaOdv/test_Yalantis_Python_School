from django.urls import include, path
from rest_framework import routers
from .views import DriverListCreateView,SingleDriverView

from . import views
# router = routers.DefaultRouter()
# router.register(r'driver', views.DriverViewSet)
app_name = "driver"
urlpatterns = [
    path('driver/', DriverListCreateView.as_view()),
    path('driver/<int:pk>', SingleDriverView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]