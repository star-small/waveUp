from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path("", views.show_products, name="show_products"),
    path("filter_by_price", views.filter_by_price)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)