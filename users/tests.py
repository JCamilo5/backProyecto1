from inspect import CO_ASYNC_GENERATOR, cleandoc
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Client, Contact

# Create your tests here.


class ClientTestCreate(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self) -> None:
        """Función que ejecuta la configuración inicial"""

        Client.objects.create(
            email="andres12@gmail.com",
            password="123"
        )
    
    def test_status(self) -> None:
        """Prueba el atributo estado del Cliente"""

        client = Client.objects.get(email='andres12@gmail.com')
        self.assertEquals(client.is_active, True)
    
class ClientTestUpdate(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self) -> None:
        """Función que ejecuta la configuración inicial"""

        client = Client.objects.create(
            email = "andres12@gmail.com",
            password = "123",
        )
        Contact.objects.create{
            user = client
        }
    
    def test_darBaja(self) -> None:
        """Prueba el atributo estado del Cliente"""

        clients = Client.objects.all()
        print("All ", clients)
        client = Client.objects.first()
        client.is_active = False
        self.assertEquals(client.is_active, False)
