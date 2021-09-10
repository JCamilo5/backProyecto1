from graphene import Field
from graphene import Mutation

from users.models import Courier
from api_graphql.data.courier.types import CourierNode
from api_graphql.data.courier.inputs import CreateCourierInput
from api_graphql.data.courier.inputs import UpdateCourierInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

# Create your mutations here


class CreateCourier(Mutation):
    """Clase para crear mensajero"""

    courier = Field(CourierNode)

    class Arguments:
        input = CreateCourierInput(required=True)

    def mutate(self, info, input: CreateCourierInput):
        courier = Courier.objects.create(**vars(input))

        return CreateCourier(courier=courier)


class UpdateCourier(Mutation):
    """Clase para actualizar mensajero"""

    courier = Field(CourierNode)

    class Arguments:
        input = UpdateCourierInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Courier.objects.filter(pk=input.get("id")).update(**input)
        courier = Courier.objects.get(pk=input.get("id"))

        return UpdateCourier(courier=courier)
