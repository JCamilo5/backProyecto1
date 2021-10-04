from graphene import (
    ID,
    String,
    InputObjectType
)

# Create your inputs types here.

class CreateProductInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación de productos
    """
    product_type = String(required=True)
    name = String(required=True)
    price = String(required=True)
    ingredients = String(required=True)
    preparation = String()
    estimated_time = String(required=True)

    # Relaciones
    enterprise_id = ID(required=True)
    to_product_id = ID(required=True)

    


class UpdateProductInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización de productos
    """
    id = ID(required=True)
    product_type = String(required=True)
    name = String()
    price = String()
    ingredients = String()
    preparation = String()
    estimated_time = String()

    # Relaciones
    enterprise_id=ID()
