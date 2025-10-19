import graphene
class Query(graphene.ObjectType):
    hello = graphene.String(description="Hello field")
    
    def resolve_hello(root,info):
        return "Hello, Graphql!"
    
schema = graphene.Schema(query=Query)