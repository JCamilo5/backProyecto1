from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import Client
from reviews.models import Review
from products.models import Image, Product
from orders.models import Order
from deliveries.models import Courier, Delivery
from enterprises.models import Enterprise

# Create your serializers here.


class SerialiserEnterprise(HyperlinkedModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'


class SerialiserDelivery(HyperlinkedModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class SerialiserCourier(HyperlinkedModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class SerialiserOrder(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SerialiserProduct(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SerialiserImage(HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class SerialiserReview(HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class SerialiserClient(HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
