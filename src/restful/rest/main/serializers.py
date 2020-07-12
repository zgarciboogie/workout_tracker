import main.models as m
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name=)
    class Meta:
        model = User
        fields = ['username', 'email']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', read_only=True)
    class Meta:
        model = m.Product
        fields = ['url', 'name', 'description', 'owner']