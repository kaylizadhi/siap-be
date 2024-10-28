"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buatAkun/', include('buatAkun.urls')),
    # path('klien/', klien_list, name='klien_list'),
    # path('klien/create/', klien_create, name='klien_create'),
    # path('klien/<int:id>/', klien_detail, name='klien_detail'),
    # path('klien/update/<int:id>/', klien_update, name='klien_update'),
    # path('klien/delete/<int:id>/', klien_delete, name='klien_delete'),
    # path('delete_akun/<int:user_id>/', delete_akun, name='delete_akun'),
    # path('', include('daftarAkun.urls')),
]
