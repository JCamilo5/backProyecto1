from datetime import date
from django import test
import graphene
from django.test import TestCase

from api_graphql.schema import Query, Mutation
from users.models import Courier


class TestGraphModelCourier(TestCase):
    def setUp(self):
        self.courier = Courier.objects.create(email="testCourier1@.com",password="1234")
        self.courier1 = Courier.objects.create(email="testCourier2@.com",password="4567")
        self.courier1 = Courier.objects.create(
            email="testCourier3@.com",password="7894", is_active=False
        )
        self.query = """query{
                            allCouriers{
                                edges{
                                    node{
                                        email
                                        }
                                    }
                                }                    
            }
            """
        self.query1 = """query{
                            allCouriers(isActive:false){
                                edges{
                                    node{
                                        email
                                        }
                                    }
                                }                    
            }
            """

        self.mutation = """
                        mutation{
                            createCourier(input:{
                                email:"testCreateCourier@.com"
                                password :"1234"
                            }){
                                courier{
                                    email
                                    isActive
                                }
                            }
                        }
        """

    def test_get_all_couriers(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "allCouriers": {
                    "edges": [
                        {"node": {"email": "testCourier1@.com"}},
                        {"node": {"email": "testCourier2@.com"}},
                        {"node": {"email": "testCourier3@.com"}},
                    ]
                }
            },
            result.data,
        )

    def test_get_courier(self):
        schema = graphene.Schema(query=Query)
        result = schema.execute(self.query1)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {"allCouriers": {"edges": [{"node": {"email": "testCourier3@.com"}}]}},
            result.data,
        )

    def test_create_courier(self):
        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(self.mutation)
        self.assertIsNone(result.errors)
        self.assertDictEqual(
            {
                "createCourier": {
                    "courier": {"email": "testCreateCourier@.com", "isActive":True}
                }
            },
            result.data,
        )
