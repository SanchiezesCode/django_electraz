from django.db import models

def get_default_country():
    return Country.objects.get(name="Россия")

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='страна')

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "стран"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "страну"
    
class City(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='город')
    country = models.ForeignKey(Country, verbose_name = "страна", on_delete=models.PROTECT, default=get_default_country)
    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "городов"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "город"

class LineMetro(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='линия метро')
   
    class Meta:
        verbose_name = 'линия метро'
        verbose_name_plural = 'линии метро'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "линий метро"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "линию метро"

class Metro(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='станция метро')
    line = models.ForeignKey(LineMetro, verbose_name = "линия метро", on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'станция метро'
        verbose_name_plural = 'станции метро'

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name_table(self):
        return "станций метро"
    
    @classmethod
    def get_verbose_name_table_add(self):
        return "станцию метро"
