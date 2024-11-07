from django.urls import path
from . import views

urlpatterns = [
    path('accounts/daftarAkun/', views.list_accounts, name='daftar-akun'),
    path('<int:id>/delete/', views.akun_delete, name='akun_delete'),
]
