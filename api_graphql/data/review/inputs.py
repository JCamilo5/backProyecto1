from graphene import InputObjectType
from graphene.types.scalars import Int
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

# Create your inputs here


class CreateReviewInput(InputObjectType):
    # Clase que encapsula los datos necesarios para la creación de valoración
    #TODO: preguntar sobre la obligatoriedad
    quality_service = String(required=True)
    presentation = String(required=True)
    preparation = String(required=True)
    ingredients = String(required=True)
    price = String(required=True)
    textures = String(required=True)
    cooking_point = String(required=True)
    comments = String(required=True)

    # relaciones
    order_id = ID(required=True)


class UpdateReviewInput(InputObjectType):
    # Clase que encapsula los datos necesarios para la actualización de valoración
    id = ID(required=True)

    quality_service = String()
    presentation = String()
    preparation = String()
    ingredients = String()
    price = String()
    textures = String()
    cooking_point = String()
    comments = String()

    # relaciones
    order_id = ID()


class DeleteReviewInput(InputObjectType):
    # Clase que encapsula los datos necesarios para eliminar una valoración
    id = ID(required=True)
