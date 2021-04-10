from graphene.relay import Node
from graphene_django import DjangoObjectType

from users.models import Client
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ClientNode(DjangoObjectType):

    class Meta:
        model = Client 
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'location': ['exact', 'icontains', 'istartswith'],
            'telephone': ['exact', 'icontains', 'istartswith'],
            'user': ['exact', 'icontains', 'istartswith'],
            'password': ['exact', 'icontains', 'istartswith'],
            'typeU': ['exact', 'icontains', 'istartswith'],
            'stateU': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
