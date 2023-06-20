from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

from dreams.models import Product, Merchant
from dreams.serializers import ProductSerializer, MerchantSerializer


class UserLoginAPIView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserRegistrationAPIView(APIView):
    def post(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')

        if User.objects.filter(username=phone).exists():
            return Response({'message': 'Phone number already registered'}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(username=phone, password=password)
        if user is not None:
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Registration failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductAPIView(APIView):
    permission_classes = IsAuthenticated

    def get(self, request):
        products = Product.objects.all()
        products_data = ProductSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = ProductSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)


class ProductUpdateDeleteAPIView(APIView):
    permission_classes = IsAuthenticated

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product_data = ProductSerializer(product, data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)

    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product_data = ProductSerializer(product, data=request.data, partial=True)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(product_data.data)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        product.delete()
        return Response(status=204)


class MerchantAPIView(APIView):
    permission_classes = IsAuthenticated

    def get(self, request):
        products = Merchant.objects.all()
        products_data = MerchantSerializer(products, many=True)
        return Response(products_data.data)

    def post(self, request):
        product_data = MerchantSerializer(data=request.data)
        product_data.is_valid(raise_exception=True)
        product_data.save()
        return Response(status=201)
