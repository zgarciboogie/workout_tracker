import main.models as m
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = m.Product
        fields = ['name', 'description']