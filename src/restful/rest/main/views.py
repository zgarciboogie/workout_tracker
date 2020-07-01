from django.shortcuts import render
import main.models as mm
import main.serializers as ms
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProductList(APIView):
    """ List all products """

    def get(self, request, format=None):
        products = mm.Product.objects.all()
        serializer = ms.ProductSerializer(products, many=True)
        return Response(serializer.data)
