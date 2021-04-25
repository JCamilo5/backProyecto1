import graphene
from django.test import TestCase

from .schema import Query
from enterprises.models import Enterprise

# Create your tests here.


class ExampleTest(TestCase):

    def setUp(self):
        """Función que ejecuta la configuración inicial"""

        Enterprise.objects.create(
            name='test 1',
            location='one location'
        )
        self.query = """
            query {
                allEnterprises {
                    edges {
                        node {
                            name
                        }
                    }
                }
            }
        """

    def test_get_all_enterprises(self):
        """Prueba la consulta de obtener todos los establecimientos"""

        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allEnterprises": {
                    "edges": [
                        {
                            "node": {
                                "name": "test 1"
                            }
                        }
                    ]
                }
            },
            result.data
        )
