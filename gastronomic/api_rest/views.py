from users.models import Client
from reviews.models import Review
from products.models import Image, Product
from orders.models import Order
from rest_framework.viewsets import ModelViewSet

from deliveries.models import Courier, Delivery
from enterprises.models import Enterprise
from api_rest.serializers import SerialiserClient, SerialiserCourier, SerialiserDelivery, SerialiserEnterprise, SerialiserImage, SerialiserOrder, SerialiserProduct, SerialiserReview

# Create your views here.


class EnterpriseViewSet(ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = SerialiserEnterprise


class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = SerialiserDelivery


class CourierViewSet(ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = SerialiserCourier


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = SerialiserOrder


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = SerialiserProduct


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = SerialiserImage


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = SerialiserReview


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SerialiserClient
