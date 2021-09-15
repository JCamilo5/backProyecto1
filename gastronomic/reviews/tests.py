from django.test import TestCase

from .models import Review
from enterprises.models import Enterprise
from users.models import Client
from products.models import Product
from orders.models import Order

# Create your tests here.


class ReviewTest(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self) -> None:
        "Funcion que ejecuta la configuración inicial"

        enterprise = Enterprise.objects.create(
            name="unicauca",
            location="Popayan"
        )

        client = Client.objects.create(
            email="example@gmail.com",
            password="123"
        )

        Product.objects.create(
            name="Producto 1",
            price=4500,
            ingredients="Sal, tomate, ajo",
            preparation="Describa aqui",
            estimated_time=4,
            enterprise_id=enterprise.pk
        )

        order = Order.objects.create(
            estimated_time="4",
            location="Ciudad prueba",
            client_id=client.pk
        )

        Review.objects.create(
            quality_service="bueno",
            presentation="bueno",
            preparation="bueno",
            ingredients="regular",
            price="malo",
            textures="regular",
            cooking_point="bueno",
            comments="Este es un comentario por defecto",
            order_id=order.pk
        )

    def test_textures(self) -> None:
        "Prueba el atributo estado de la Review"

        review = Review.objects.get(quality_service="bueno")
        self.assertEquals(review.textures, "regular")
