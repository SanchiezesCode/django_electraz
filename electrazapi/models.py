from django.db import models

class CategoryProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ManufacturerProduct(models.Model):
    id = models.AutoField(primary_key=True)
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

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='поставщик')
    link = models.URLField(blank=True, default='', verbose_name='сайт')
    
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

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(CategoryProduct, on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(ManufacturerProduct, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    old_price = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    additional_info = models.TextField(blank=True)
    meta_tag = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)
    meta_keywords = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    photo = models.ImageField(upload_to='products/', blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductSupplier(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    link = models.CharField(max_length=200)

    class Meta:
        unique_together = ('product', 'supplier')

    def __str__(self):
        return f"{self.product.name} - {self.supplier.name}"



class Client(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, blank=True)  # Поле фамилии необязательное
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)  # Поле email необязательное

    def __str__(self):
        return self.first_name

    
class asdf(models.Model):
    a = models.CharField(max_length=100)
    email = models.EmailField()
    url = models.URLField()
        