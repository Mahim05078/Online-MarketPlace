# from django.contrib import admin
from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', 'admin.site.urls'),
    path('register.html/', include('register_app.urls')),
    path('login.html/', include('login_app.urls')),
    path('', views.HomeView.as_view(), name="home"),
    path('about.html/', views.AboutView.as_view(), name="about"),
    path('index.html/', views.index),
    path('application.html/', views.application),
    path('contact.html/', views.contact),
    path('care.html/', views.care),
    path('codes.html/', views.codes),
    path('faqs.html/', views.faqs),
    path('hold.html/', views.hold),
    path('kitchen.html/', views.kitchen),
    path('offer.html/', views.offer),
    path('shipping.html/', views.shipping),
    path('wishlist.html/', views.wishlist),
    path('terms.html/', views.terms),
    path('single.html/', views.single),
    path('shoplisttorent.html/', views.shoplisttorent),
    # path(r'shoplisttorent.html/?*=click+me', views.application),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
