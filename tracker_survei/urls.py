from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_list_survei, name='list-survei'),
    path('<int:survei_id>/', views.get_tracker_detail, name='tracker-detail'),
    path('<int:survei_id>/administrasi-awal/', views.update_administrasi_status, name='update-administrasi'),
    path('<int:survei_id>/administrasi-akhir/', views.update_administrasi_akhir_status, name='update-administrasi-akhir'),
    path('<int:survei_id>/logistik/', views.update_logistik_status, name='update-logistik'),
    path('<int:survei_id>/pengendali-mutu/', views.update_pengendali_mutu_status, name='update-pengendali-mutu'),
    path('dashboard/', views.get_list_dashboard)
]