from django.urls import path  
from .views import buat_akun
# from accounts.views import login_view

urlpatterns = [
    path('', buat_akun, name='buat_akun'),
]
