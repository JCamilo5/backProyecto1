from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from orders.models import Report

# Create your objects types here.


class ReportNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Report
        filter_fields = {
            "id_interprise": ["exact", "icontains", "istartswith"],
            "report_type": ["exact", "icontains", "istartswith"],
            "report_information": ["exact", "icontains", "istartswith"],
        }
        interfaces = (Node,)
        connection_class = TotalCountConnection
