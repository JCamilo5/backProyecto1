from graphene import Schema

from api_graphql.schema import Query, Mutation

# Schema definition


schema = Schema(query=Query, mutation=Mutation)
