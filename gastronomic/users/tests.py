from django.test import TestCase
from .models import Courier
# Create your tests here.


class testModelUserCourier(TestCase):
    def setUp(self):
        """Creacion de un mensajero"""
        self.courier =  Courier.objects.create(email="testCourier@local.com")
        return super().setUp()

    def test_Is_Staff_Default(self):
        """Un mensajero no puede ser administrador"""
        self.assertFalse(self.courier.is_staff)

    def test_Is_active_Default(self):
        """Al momento de la creacion de un mensajero esté debe quedar activo"""
        self.assertTrue(self.courier.is_active)