from django.conf.urls.static import static
from django.conf import settings
from django.urls import path  # , include
# from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.show_main, name="main_url"),
    path("catalog/", views.show_products, name="catalog_url"),
    path("product/<slug:slug>/", views.show_product, name="product_url"),
    path("policy", views.show_policy, name='policy_url'),
    path("about_us", views.show_about_us, name='about_us_url'),
    path("contacts", views.show_contacts, name='contacts_url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
