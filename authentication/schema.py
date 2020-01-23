import graphene
from graphene_django import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(object):
    users = graphene.List(UserType)
    user = graphene.Field(username=graphene.String())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_user(self, info, username):
        return User.objects.get(username=username)
    
