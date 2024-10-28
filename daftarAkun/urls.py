from django.urls import path
from . import views

urlpatterns = [
    path('daftarAkun/', views.list_accounts, name='daftar-akun'),
]
