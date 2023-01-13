from django.db import models

class Language(models.Model):
    user_ip = models.CharField(null=True, blank=False, max_length=32)
    LANG_CHOICES = [(0, 'uz'), (1, 'ru'), (2, 'en')]
    lang = models.IntegerField(null=True, blank=True, choices=LANG_CHOICES)

class Product(models.Model):
    title_uz = models.CharField(null=True, blank=False, max_length=255, verbose_name='Название (UZ)')
    title_ru = models.CharField(null=True, blank=False, max_length=255, verbose_name='Название (RU)')
    title_en = models.CharField(null=True, blank=False, max_length=255, verbose_name='Название (ENG)')
    price = models.BigIntegerField(null=True, blank=True, verbose_name='Цена')
    photo = models.FileField(upload_to='photos/product', blank=False, verbose_name='Фото')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
