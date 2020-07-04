from django.shortcuts import render
import main.models as mm
import main.serializers as ms
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserList(APIView):
    """ List all users """
    
    def get(self, request, format=None):
        users = None
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        elif request.user.is_superuser:
            users = User.objects.all()
        else:
            users = User.objects.all().filter(username=request.user.username)
        if users:
            serializer = ms.UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Unable to process request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductList(APIView):
    """ List all products """

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        products = mm.Product.objects.all().filter(owner=request.user)
        serializer = ms.ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ms.ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """ Product detail """

    def get_object(self, pk):
        try:
            return mm.Product.objects.get(pk=pk)
        except mm.Product.DoesNotExist:
            return Response({'detail': 'Object does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        product = self.get_object(pk)
        serializer = ms.ProductSerializer(product)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        product = self.get_object(pk)
        serializer = ms.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)