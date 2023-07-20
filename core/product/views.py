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
    # print(request.method)
    if request.method == "POST":
        data = request.POST
        # print(data)
        time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M")
        print(data["name"])
        tb.load_data(data)
        send_mail(data)
        return redirect("main_url")
    return render(request, "index.html", context={"products": products})


def show_products(request):
    products = Product.objects.all().order_by("date")
    rows = read_from_csv() if os.path.exists(BASE_DIR / "files/file.csv") else None
    dict_to_db(rows) if rows else None

    if request.method == "POST":
        data = request.POST
        filtered = Product.objects.all()
        categories = []
        if data.get("Светильники"):
            categories.append("Светильник")
        if data.get("Плафоны"):
            categories.append("Плафон")
        if data.get("Лампы"):
            categories.append("Лампа")
        if categories:
            filtered = filtered.filter(category__name__in=categories)
            print(filtered)
            return render(request, "pages/catalog.html", context={"products": filtered})

        if data.get("name"):
            tb.load_data(data)
            send_mail(data)
            return redirect("main_url")

    return render(request, "pages/catalog.html", context={"products": products})


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
