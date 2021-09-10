from django.test import TestCase

from .models import Enterprise

# Create your tests here.


class EnterpriseTest(TestCase):
    """Clase que prueba los atributos del modelo"""

    def setUp(self) -> None:
        """Función que ejecuta la configuración inicial"""

        Enterprise.objects.create(
            name="enterprise 1",
            location="avenida siempre viva 742",
        )

    def test_status(self) -> None:
        """Prueba el atributo estado del establecimiento"""

        enterprise = Enterprise.objects.get(name="enterprise 1")
        self.assertEquals(enterprise.status, True)
