import graphene
from django.test import TestCase

from api_graphql.schema import Query
from users.models import Client
from orders.models import Order
from reviews.models import Review
from products.models import Product
from enterprises.models import Enterprise

# Create your tests here.


class OrderTest(TestCase):
    """Funcion que ejecuta la configuracion for OrderTest"""

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

        self.query = """
			query{
				allOrders{
					edges{
						node{
                            location
						}
					}
				}
			}
		"""

    def test_get_all_orders(self):
        """Prueba la consulta de obtener todos los orders"""

        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allOrders": {
                    "edges": [
                        {
                            "node": {
                                "location": "Ciudad prueba"
                            }
                        }
                    ]
                }
            },
            result.data
        )
