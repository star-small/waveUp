from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.show_main, name="products_url"),
    path("catalog/", views.show_products, name="catalog_url"),
    path("product/<slug:slug>/", views.show_product, name="product_url")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
