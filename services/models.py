from itertools import count
from django.db import models

class ServiceCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='категория')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "категорий"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "категории"

class Service(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='услуга')
    category = models.ForeignKey(ServiceCategory, verbose_name = "категория", on_delete=models.CASCADE)
    cost = models.PositiveIntegerField(verbose_name='цена', blank=True, default=0)
    UNIT_TYPE_CHOICES = (
        ('м.', 'м.'),
        ('шт.', 'шт.')
    )
    unit = models.CharField(default='шт.', max_length=10, choices=UNIT_TYPE_CHOICES, verbose_name = 'единица измерения')
   
    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "услуг"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "услуги"
