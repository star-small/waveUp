from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_products, name="show_products"),
    path("filter_by_price", views.filter_by_price)
]

