from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from deliveries.models import Delivery

# Create your objects types here.


class DeliveryNode(DjangoObjectType):

    class Meta:
        model = Delivery 
        filter_fields = {
            'status': ['exact', 'icontains', 'istartswith'],
            'delivery_time': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
