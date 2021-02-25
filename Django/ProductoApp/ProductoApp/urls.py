from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('apps.gestionApp.urls')),
    path('ventas/', include('apps.ventas.urls')),
    path('', views.index, name = 'homepage'),
]
