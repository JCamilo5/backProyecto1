from graphene.relay import Node
from graphene_django import DjangoObjectType

from enterprises.models import Management
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class ManagementNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Management
        filter_fields = {
            'date': ['exact'],
            'status': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
