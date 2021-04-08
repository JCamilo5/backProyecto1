from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from products.models import Product

# Create your objects types here.


class ProductNode(DjangoObjectType):

    class Meta:
        model = Product 
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'price': ['exact'],
            'ingredients': ['exact', 'icontains', 'istartswith'],
            'preparation': ['exact', 'icontains', 'istartswith'],
            'estimated_time': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
