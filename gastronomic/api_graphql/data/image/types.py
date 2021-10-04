from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from products.models import Image

# Create your objects types here.

class ImageNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Image
        filter_fields = {
            
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
    
