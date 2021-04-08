from graphene import Schema

from api_graphql.schema import Query, Mutation


schema = Schema(query=Query, mutation=Mutation)
