from rest_framework.serializers import ModelSerializer

from dreams.models import Product, Merchant


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class MerchantSerializer(ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
