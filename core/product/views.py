from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def show_products(request):
    products = Product.objects.all()
    return render(request, "pages/products.html", context={"products": products})

def load_excel():
