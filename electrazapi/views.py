# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from .models import CategoryProduct, Country, ManufacturerProduct, Supplier, Product, ProductSupplier
from .serializers import CategoryProductSerializer, CountrySerializer, ManufacturerProductSerializer, SupplierSerializer, ProductSerializer, ProductSupplierSerializer

class CategoryProductViewSet(viewsets.ModelViewSet):
    queryset = CategoryProduct.objects.all()
    serializer_class = CategoryProductSerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ManufacturerProductViewSet(viewsets.ModelViewSet):
    queryset = ManufacturerProduct.objects.all()
    serializer_class = ManufacturerProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSupplierViewSet(viewsets.ModelViewSet):
    queryset = ProductSupplier.objects.all()
    serializer_class = ProductSupplierSerializer