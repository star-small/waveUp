from django.conf.urls.static import static
from django.conf import settings
from django.urls import path  # , include
# from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("catalog/", views.show_products, name="catalog_url"),
    path("", views.PageRenderer.as_view(), name="main_url"),
    path("policy", views.PageRenderer.as_view(), name="policy_url"),
    path("about_us", views.PageRenderer.as_view(), name="about_us_url"),
    path("contacts", views.PageRenderer.as_view(), name="contacts_url"),
    path("product/<slug:slug>/", views.show_product, name="product_url"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
