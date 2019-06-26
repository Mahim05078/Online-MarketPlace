from django.urls import path
#from django.contrib import admin
from . import views


urlpatterns = [
    # path('admin/', 'admin.site.urls'),
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
]
