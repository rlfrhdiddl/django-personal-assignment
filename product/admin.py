from django.contrib import admin
from .models import Product

#이건 이해가 잘 가지 않음. 확인필요.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')


admin.site.register(Product, ProductAdmin)