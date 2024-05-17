from logging import PlaceHolder
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('service_categorys/', ShowServiceCategorys, name='service_categorys'),
    path('services', ShowServices, name='services'),


    # path('product_list/', ShowProduct_list, name='product_list'),
    # path('product_category/', ShowProduct_category, name='product_category'),
    # path('product_manufacturer/', ShowProduct_manufacturer, name='product_manufacturer'),
    # path('manufacturer_country/', ShowManufacturer_country, name='manufacturer_country'),
    # path('supplier_list/', ShowSupplier_list, name='supplier_list'),
    # path('product_add/', ShowProduct_add, name='product_add'),
    # path('crm_clients/', crm_clients, name='crm_clients'),  # URL для представления clients_view
    # path('crm/leads/', ShowCrm_leads, name='crm_leads'),
    # path('crm/add/', ShowCrm_add, name='crm_add'),
    # path('maincalc/', ShowMainCalcPage),
    # path('upload/', upload_file, name='upload_file'),
]