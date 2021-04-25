from graphene.relay import Node
from graphene_django import DjangoObjectType

from users.models import Client
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ClientNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Client
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith'],
            'password': ['exact', 'icontains', 'istartswith'],
            'last_login': ['exact'],
            'is_active': ['exact', 'icontains', 'istartswith'],
            'is_staff': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
