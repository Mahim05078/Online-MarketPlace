from django.urls import path
# from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', 'admin.site.urls'),
    path('register.html/', views.registerView.as_view(), name="register"),
    path('login.html/', views.login),
    path('', views.HomeView.as_view(), name="home"),
    path('about.html/', views.AboutView.as_view(), name="about"),
    path('index.html/', views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
