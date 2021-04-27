from graphene.relay import Node
from graphene_django import DjangoObjectType

from users.models import Contact
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ContactNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Contact
        filter_fields = {
            'names': ['exact', 'icontains', 'istartswith'],
            'lastnames': ['exact', 'icontains', 'istartswith'],
            'location': ['exact', 'icontains', 'istartswith'],
            'telephone': ['exact', 'icontains', 'istartswith'],
            'license_plate': ['exact', 'icontains', 'istartswith'],
            'created': ['exact'],
            'updated': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
