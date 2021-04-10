from django.urls.conf import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from .views import (
    EnterpriseViewSet,
    DeliveryViewSet,
    CourierViewSet,
    OrderViewSet,
    ProductViewSet,
    AccompanimentViewSet,
    ImageViewSet,
    ReviewViewSet,
    ClientViewSet
)

# Create your urls here.


router = DefaultRouter()

router.register('enterprises', EnterpriseViewSet)
router.register('deliveries', DeliveryViewSet)
router.register('couries', CourierViewSet)
router.register('orders', OrderViewSet)
router.register('products', ProductViewSet)
router.register('accompaniments', AccompanimentViewSet)
router.register('images', ImageViewSet)
router.register('reviews', ReviewViewSet)
router.register('clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]