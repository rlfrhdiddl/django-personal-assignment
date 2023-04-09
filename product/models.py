from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 16, verbose_name="상품명")
    code = models.CharField(max_length = 16, verbose_name="상품코드")
    description = models.CharField(max_length = 16, verbose_name="상품설명")
    price = models.CharField(max_length = 16, verbose_name="상품가격")
    stock = models.CharField(max_length = 16, verbose_name="재고")
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField( max_length=1, choices=sizes)