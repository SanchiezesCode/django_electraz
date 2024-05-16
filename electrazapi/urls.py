# urls.py приложения
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryProductViewSet, CountryViewSet, ManufacturerProductViewSet, SupplierViewSet, ProductViewSet, ProductSupplierViewSet

router = DefaultRouter()
router.register(r'categoryproduct', CategoryProductViewSet)
router.register(r'country', CountryViewSet)
router.register(r'manufacturerproduct', ManufacturerProductViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'product', ProductViewSet)
router.register(r'productsupplier', ProductSupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
