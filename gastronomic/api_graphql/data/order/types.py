from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from orders.models import Order

# Create your objects types here.


class OrderNode(DjangoObjectType):

    class Meta:
        model = Order 
        filter_fields = {
            'date': ['exact', 'icontains', 'istartswith'],
            'estimated_time': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
