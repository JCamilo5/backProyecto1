from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from products.models import Product

# Create your objects types here.


class ProductNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Product
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'price': ['exact'],
            'ingredients': ['exact', 'icontains', 'istartswith'],
            'preparation': ['exact', 'icontains', 'istartswith'],
            'estimated_time': ['exact']
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
