from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

# Create your inputs types here.


class CreateCourierInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios para la
    creacion de mensajero
    """

    email = String(required=True)
    password = String(required=True)


class UpdateCourierInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de mensajero
    """

    id = ID(required=True)
    password = String()
    is_active = Boolean()
    is_available = Boolean()
