import graphene
import tracks.schema
import users.schema
import graphql_jwt


class AuthMutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


class Query(users.schema.Query, tracks.schema.Query, graphene.ObjectType):
    pass


class Mutation(AuthMutation, users.schema.Mutation, tracks.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
