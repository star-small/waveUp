import os

from django.views.generic import View
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .forms import UserForm
from .modules.utils import *
from .senders import AllSender

BASE_DIR = Path(__file__).resolve().parent.parent


class PageRenderer(PageRendererMixin, View):
    model = Product
    obj = model.objects.all().order_by("price")[0:5]


def show_products(request):
    products = Product.objects.all().order_by("date")
    rows = read_from_csv() if os.path.exists(BASE_DIR / "files/file.csv") else None
    dict_to_db(rows) if rows else None
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        if data.get("filter"):
            category_list = data.getlist("filter")
            filtered = products.filter(category__name__in=category_list)
            return render(
                request,
                "pages/catalog.html",
                context={"products": filtered, "categories": categories},
            )
        else:  # Обработка и отправка заявок
            sender = AllSender(request.POST)
            sender.send()
            return redirect("catalog_url")
    return render(
        request,
        "pages/catalog.html",
        context={"products": products, "categories": categories},
    )


def show_product(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == "POST":
        sender = AllSender(request.POST)
        print(request.POST)
        sender.send()
        return redirect("catalog_url")
    return render(request, "pages/item.html", context={"product": product})
