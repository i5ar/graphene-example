import graphene

import ingredients.schema


class Query(ingredients.schema.Query, graphene.ObjectType):
    """

    .. _Graphene Django Queries:
        http://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/

    """

    pass


class Mutation(ingredients.schema.Mutation, graphene.ObjectType):
    """

    .. _Graphene Mutations:
        http://docs.graphene-python.org/en/latest/types/mutations/

    """

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
