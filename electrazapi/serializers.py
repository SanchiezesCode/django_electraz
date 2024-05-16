# serializers.py
from rest_framework import serializers
from .models import CategoryProduct, Country, ManufacturerProduct, Supplier, Product, ProductSupplier

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ManufacturerProductSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta:
        model = ManufacturerProduct
        fields = ['id', 'name', 'country']

    def create(self, validated_data):
        country = validated_data.pop('country')
        manufacturer_product = ManufacturerProduct.objects.create(country=country, **validated_data)
        return manufacturer_product

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'link']
        extra_kwargs = {
            'link': {'required': False}
        }

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSupplier
        fields = '__all__'