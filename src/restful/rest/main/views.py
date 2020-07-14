from django.shortcuts import render
import main.models as mm
import main.serializers as ms
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.request import Request
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
            users = User.objects.filter(username=request.user.username)
        if users:
            serializer = ms.UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Unable to process request.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductList(APIView):
    """ List all products """

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        products = mm.Product.objects.filter(owner=request.user)
        serializer = ms.ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ms.ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """ Product detail """

    def get_object(self, pk, user):
        try:
            product = mm.Product.objects.get(pk=pk)
            if user.username != product.owner.username:
                return None
            return product
        except mm.Product.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        product = self.get_object(pk, request.user)
        if not product:
            return Response({'detail': 'Product does not exist or you are not authorized for this action.'}, status=status.HTTP_418_IM_A_TEAPOT)
        serializer = ms.ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        product = self.get_object(pk, request.user)
        serializer = ms.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk, request.user)
        if not snippet:
            return Response({'detail': 'Product does not exist or you are not authorized for this action.'}, status=status.HTTP_418_IM_A_TEAPOT)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExcersiseList(APIView):
    """ Lists all excersises belonging to a user """

    def get(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        excersises = mm.Exercise.objects.filter(owner=request.user)
        serializer = ms.ExcersiseSerializer(excersises, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ms.ExcersiseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcersiseDetail(APIView):
    """ Excersise detail """

    def get_object(self, pk, user):
        try:
            excersise = mm.Exercise.objects.get(pk=pk)
            if user.username != excersise.owner.username:
                return None
            return excersise
        except mm.Exercise.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        excersise = self.get_object(pk, request.user)
        if not excersise:
            return Response({'detail': 'Product does not exist or you are not authorized for this action.'}, status=status.HTTP_418_IM_A_TEAPOT)
        serializer = ms.ExcersiseSerializer(excersise, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if request.user.is_anonymous:
            return Response({'detail': 'User is not authenticated.'}, status=status.HTTP_403_FORBIDDEN)
        excersise = self.get_object(pk, request.user)
        if not excersise:
            return Response({'detail': 'Product does not exist or you are not authorized for this action.'}, status=status.HTTP_418_IM_A_TEAPOT)
        serializer = ms.ExcersiseSerializer(excersise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk, request.user)
        if not snippet:
            return Response({'detail': 'Product does not exist or you are not authorized for this action.'}, status=status.HTTP_418_IM_A_TEAPOT)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)