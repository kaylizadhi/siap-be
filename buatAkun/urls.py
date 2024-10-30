from django.urls import path  
from .views import buat_akun
# from accounts.views import login_view

urlpatterns = [
    path('api/buatAkun/', buat_akun, name='buat_akun'),
]
