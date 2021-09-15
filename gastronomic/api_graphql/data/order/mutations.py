from graphene import Field
from graphene import Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from orders.models import Order
from api_graphql.data.order.types import OrderNode
from api_graphql.data.order.inputs import CreateOrderInput
from api_graphql.data.order.inputs import UpdateOrderInput
from api_graphql.utils import delete_attributes_none
from api_graphql.utils import transform_global_ids

# Create your mutation here


class CreateOrder(Mutation):
    """Clase para crear un pedido"""
    order = Field(OrderNode)

    class Arguments:
        input = CreateOrderInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        order = Order.objects.create(**input)

        return CreateOrder(order=order)


class UpdateOrder(Mutation):
    """Clase para realizar la actualización de un pedido"""
    order = Field(OrderNode)

    class Arguments:
        input = UpdateOrderInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Order.objects.filter(pk=input.get("id")).update(**input)
        order = Order.objects.get(pk=input.get("id"))

        return UpdateOrder(order=order)


class DeleteOrder(Mutation):
    """Clase para eliminar un pedido"""

    order = Field(OrderNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            order = Order.objects.get(pk=input)
            Order.objects.filter(pk=input).delete()
        except Order.DoesNotExist:
            raise GraphQLError("Order does not delete")

        return CreateOrder(order=order)
