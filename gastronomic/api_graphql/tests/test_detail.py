import graphene
from django.db.utils import IntegrityError
from django.test import TestCase

from api_graphql.schema import Query

from users.models import Client
from orders.models import Order
from orders.models import Detail
from reviews.models import Review
from products.models import Product
from enterprises.models import Enterprise

# Create your tests here.


class DetailTest(TestCase):
    """Funcion que ejecuta la configuración for DetailTest"""

    def setUp(self):

        enterprise = Enterprise.objects.create(
            name='unicauca',
            location='Popayan'
        )

        client = Client.objects.create(
            email="example@gmail.com",
            password="123"
        )

        product = Product.objects.create(
            name="Producto 1",
            price=4500,
            ingredients="Sal, tomate, ajo",
            preparation="Describa aqui",
            estimated_time=4,

            # Relaciones
            enterprise_id=enterprise.pk
        )

        order = Order.objects.create(
            estimated_time="4",
            location="Ciudad prueba",

            # Relaciones
            client_id=client.pk
        )

        Detail.objects.create(
            quantity=22,
            product_id=product.pk,

            # Relaciones
            order_id=order.pk
        )
        self.query = """
			query{
				allDetails{
					edges{
						node{
                            quantity
						}
					}
				}
			}
		"""
  
    def test_get_all_details(self):
        """Prueba la consulta de obtener todos los details"""

        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allDetails": {
                    "edges": [
                        {
                            "node": {
                                "quantity": 22
                            }
                        }
                    ]
                }
            },
            result.data
        )
