from django.urls import path
from .views import delete_akun, confirm_delete_akun  

urlpatterns = [
    path('hapus/<int:user_id>/', confirm_delete_akun, name='confirm_delete_akun'),  
    path('hapus/aksi/<int:user_id>/', delete_akun, name='delete_akun'),  
]
