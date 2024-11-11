from django.urls import path
from . import views

urlpatterns = [
    path('api/daftarAkun/', views.akun_list, name='akun_list'),
    path('<int:id>/delete/', views.akun_delete, name='akun_delete'),
    path('api/searchAkun/', views.search_akun, name='search_akun'),
]
