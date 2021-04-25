from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from orders.models import Order

# Create your objects types here.


class OrderNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Order
        filter_fields = {
            'date': ['exact'],
            'status': ['exact'],
            'estimated_time': ['exact'],
            'location': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
