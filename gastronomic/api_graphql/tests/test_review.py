import graphene
from django.test import TestCase

from api_graphql.schema import Query
from users.models import Client
from orders.models import Order
from reviews.models import Review
from products.models import Product
from enterprises.models import Enterprise


class ReviewTest(TestCase):
    """Funcion que ejecuta la configuracion for ReviewTest"""

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

        Review.objects.create(
            quality_service='bueno',
            presentation='bueno',
            preparation='bueno',
            ingredients='regular',
            price='malo',
            textures='regular',
            cooking_point='bueno',
            comments='Este es un comentario por defecto',

            # Relaciones
            order_id=order.pk
        )

        self.query = """
			query{
				allReviews{
					edges{
						node{
                            qualityService
						}
					}
				}
			}
		"""

    def test_get_all_reviews(self):
        """Prueba la consulta de obtener todos los reviews"""

        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allReviews": {
                    "edges": [
                        {
                            "node": {
                                "qualityService": "BUENO"
                            }
                        }
                    ]
                }
            },
            result.data
        )
