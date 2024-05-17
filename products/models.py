from itertools import product
from django.utils import timezone
from django.db import models
from locations.models import City, Country
from django.core.exceptions import ValidationError

def get_default_city():
    return City.objects.get(name="Москва")

def get_default_category():
    return ProductCategory.objects.get(name="")

class ProductSupplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='поставщик')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='номер телефона')
    url = models.URLField(blank=True, default='', verbose_name='сайт')
    discount = models.PositiveIntegerField(verbose_name='скидка %', default=0)
    city = models.ForeignKey(City, verbose_name = "город", on_delete=models.PROTECT, default=get_default_city)
    address = models.CharField(max_length=20, blank=True, verbose_name='адрес')
    additionall = models.TextField(blank=True, verbose_name='дополнительно', default='')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

    @classmethod
    def get_verbose_name_table(self):
        return "поставщиков"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "поставщика"
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='категория')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=get_default_category, verbose_name='Родительская категория')
    
    
    def clean(self):
        if self.parent and self.parent.pk == self.pk:
            raise ValidationError({'parent': 'Родительской категорией не может быть текущая категория.'})

    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    @classmethod
    def get_verbose_name_table(self):
        return "категорий"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "категорию"
    
class ProductManufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name='производитель')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'

    @classmethod
    def get_verbose_name_table(self):
        return "производителей"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "производителя"
    
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='товар')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, default=get_default_category, verbose_name='категория')
    manufacturer = models.ForeignKey(ProductManufacturer, on_delete=models.PROTECT, verbose_name='производитель')
    price = models.PositiveIntegerField(verbose_name='цена', default=0)
    old_price = models.PositiveIntegerField(verbose_name='старая цена', default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    price_updated_at = models.DateTimeField(verbose_name='дата изменения цены', blank=True, auto_now_add=True,)
    additional_info = models.TextField(blank=True, verbose_name='дополнительно')
    meta_tag = models.CharField(max_length=100, blank=True, verbose_name='тег')
    meta_description = models.CharField(max_length=200, blank=True, verbose_name='описание')
    meta_keywords = models.CharField(max_length=200, blank=True, verbose_name='ключевые слова')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='идентификатор url')
    availability = models.PositiveIntegerField(default=0, verbose_name='в наличии')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):

        if self.pk:
            # Объект модели уже существует
            previous_price = Product.objects.get(pk=self.pk).price
            if self.price != previous_price:
                self.old_price = previous_price
                self.price_updated_at = timezone.now()    
        else:
            self.old_price = self.price
        super().save(*args, **kwargs)


    @classmethod
    def get_verbose_name_table(self):
        return "товаров"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "товар"