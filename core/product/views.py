import os

from django.shortcuts import render, redirect
from .modules.sheets import Table
from .modules.mail import send_mail
# from django.contrib.auth.models import User
# from .forms import UserForm
from .modules.utils import *

BASE_DIR = Path(__file__).resolve().parent.parent
tb = Table()  # google sheets


def show_main(request):
    products = Product.objects.all().order_by("price")[0:5]
    if request.method == "POST":
        data = request.POST
        print(data["name"])
        tb.load_data(data)
        send_mail(data)
        return redirect("main_url")
    return render(request, "index.html", context={"products": products})


def show_products(request):
    products = Product.objects.all().order_by("date")
    rows = read_from_csv() if os.path.exists(BASE_DIR / "files/file.csv") else None
    dict_to_db(rows) if rows else None
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        if data.get("filter"):
            print(data)
            category_list = data.getlist("filter")
            filtered = products.filter(category__name__in=category_list)
            return render(
                request,
                "pages/catalog.html",
                context={"products": filtered, "categories": categories},
            )
    return render(
        request,
        "pages/catalog.html",
        context={"products": products, "categories": categories},
    )


def show_contacts(request):
    if request.method == "POST":
        data = request.POST
        time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
        send_mail(data)
        return redirect("main_url")
    return render(request, "pages/contacts.html")


def show_product(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, "pages/order.html", context={"product": product})


def show_policy(request):
    return render(request, "pages/policy.html")


def show_about_us(request):
    return render(request, "pages/about_us.html")
