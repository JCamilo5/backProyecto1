from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from enterprises.models import Enterprise

# Create your objects types here.


class EnterpriseNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Enterprise
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'historical_review': ['exact', 'icontains', 'istartswith'],
            'location': ['exact', 'icontains', 'istartswith'],
            'business_hours': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
            'created': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
