from django.db import models
import string
import re
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver

TRANSLATION_TABLE = str.maketrans(
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA"
)

def slugify(value):
    value = str(value).lower()
    value = re.sub(r'[^\w\s-]', '', value)
    value = re.sub(r'[-\s]+', '-', value)
    value = value.strip('-')
    value = value.translate(TRANSLATION_TABLE)
    value = ''.join(c for c in value if c in string.ascii_letters + string.digits + '-')
    return value

    # def save(self, *args, **kwargs):
    #     if not self.slug_field:
    #         self.slug_field = slugify(self.char_field)
    #     super().save(*args, **kwargs)





class Client(models.Model):
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, blank=True)  # Поле фамилии необязательное
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)  # Поле email необязательное

    def __str__(self):
        return self.first_name



    



    