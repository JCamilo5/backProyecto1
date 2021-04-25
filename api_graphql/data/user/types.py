from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from profiles.models import UserProfile

# Create your objects types here.


class UserNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = UserProfile
        filter_fields = {
            'email': ['exact', 'icontains', 'istartswith'],
            'password': ['exact', 'icontains', 'istartswith'],
            'type': ['exact', 'icontains', 'istartswith'],
            'last_login': ['exact'],
            'is_active': ['exact'],
            'is_superuser': ['exact'],
            'is_staff': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
