from graphene import Int
from graphene import Connection

# Create your connections here


class TotalCountConnection(Connection):
    """
    Clase que permite saber el total de registros
    por cada consulta que se realice
    """
    total_count = Int()

    class Meta:
        abstract = True

    def resolve_total_count(self, info) -> int:
        """
        Función que retorna el número de registros
        """
        return self.length
