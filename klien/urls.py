from django.contrib import admin
from django.urls import path
from .views import klien_list, klien_create, klien_detail, klien_update, klien_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('klien/', klien_list, name='klien_list'),
    path('klien/create/', klien_create, name='klien_create'),
    path('klien/<int:id>/', klien_detail, name='klien_detail'),
    path('klien/update/<int:id>/', klien_update, name='klien_update'),
    path('klien/delete/<int:id>/', klien_delete, name='klien_delete'),
]
