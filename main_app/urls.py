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
    # path('index.html/', views.login),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
