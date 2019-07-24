from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    # path(r'shopowner.html/', views.ShopView.as_view(), name="shopowner"),
    path(r'shopowner.html/', views.index),
    path(r'Inventory.html/', views.inventoryView),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)