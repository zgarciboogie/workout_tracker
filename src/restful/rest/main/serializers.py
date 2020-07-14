import main.models as m
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Users serializer """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """ Products serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
    class Meta:
        model = m.Product
        fields = ['url', 'name', 'description', 'owner']

class ExcersiseSerializer(serializers.HyperlinkedModelSerializer):
    """ Excersise serializer """
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='excersise-detail', read_only=True)
    class Meta:
        model = m.Exercise
        fields = ['owner', 'url', 'name', 'description', 'feature']