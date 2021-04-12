from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from deliveries.models import Courier

# Create your objects types here.


class CourierNode(DjangoObjectType):

    class Meta:
        model = Courier 
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'location': ['exact', 'icontains', 'istartswith'],
            'telephone': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
