from graphene import Mutation
from graphene import Field
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from orders.models import Detail
from api_graphql.data.detail.types import DetailNode
from api_graphql.data.detail.inputs import CreateDetailInput
from api_graphql.data.detail.inputs import UpdateDetailInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none


class CreateDetail(Mutation):
    """Clase para crear detalles"""

    detail = Field(DetailNode)

    class Arguments:
        input = CreateDetailInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        detail = Detail.objects.create(**input)

        return CreateDetail(detail=detail)


class UpdateDetail(Mutation):
    """Clase para actualizar detalles"""

    detail = Field(DetailNode)

    class Arguments:
        input = UpdateDetailInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Detail.objects.filter(pk=input.get("id")).update(**input)
        detail = Detail.objects.get(pk=input.get("id"))

        return UpdateDetail(detail=detail)


class DeleteDetail(Mutation):
    """Clase para eliminar detalle"""

    detail = Field(DetailNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]

        try:
            detail = Detail.objects.get(pk=input)
            Detail.objects.filter(pk=input).delete()
        except Detail.DoesNotExist:
            raise GraphQLError("Detail does not delete")

        return CreateDetail(detail=detail)
