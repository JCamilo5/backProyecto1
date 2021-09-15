from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from deliveries.models import Delivery

# Create your objects types here.


class DeliveryNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Delivery
        filter_fields = {
            'status': ['exact'],
            'delivery_time': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
