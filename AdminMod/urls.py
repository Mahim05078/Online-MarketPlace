from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    path(r'admin.html/', views.AdminView.as_view(), name="admin"),
    path(r'applicationview.html/', views.applicationview),
    path(r'Shopmanagement.html/', views.Shopmanagement),
    path(r'Shopstatistics.html/', views.Shopstatistics),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
