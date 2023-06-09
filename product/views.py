from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from .forms import RegisterForm
from django.views.generic.edit import FormView

class ProductRegister(FormView):
    template_name = 'product_register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            stock = form.data.get('stock'),
            description = form.data.get('description')
        )
        product.save()
        return super().form_valid(form)