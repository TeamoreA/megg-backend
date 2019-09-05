
import graphene

import users.schema

from graphene_django.debug import DjangoDebug


class Query(users.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, graphene.ObjectType,):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)