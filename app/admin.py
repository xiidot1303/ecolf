from django.contrib import admin
from app.models import *
from app.forms import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en', 'price', 'photo')
    search_fields = ['title_uz', 'title_ru', 'title_en']
    form = ProductForm



# admin.site.register(Language, LanguageAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_header = 'Ecolf admin'
admin.site.site_title = 'Ecolf'