
from graphene.types.scalars import Int
from graphene import InputObjectType
from graphene.types.scalars import ID


class CreateDetailInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de detalles
    """

    quantity = Int(required=True)

    # Relaciones o foraneas.
    order_id = ID(required=True)
    product_id = ID(required=True)


class UpdateDetailInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para
    la actualización de establecimientos
    """
    id = ID(required=True)
    quantity = Int()

    # Relaciones o foraneas.
    order_id = ID()
    product_id = ID()
