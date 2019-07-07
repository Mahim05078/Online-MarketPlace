from . import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login),
    path('register.html', include('register_app.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
