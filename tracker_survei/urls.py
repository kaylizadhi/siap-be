from django.urls import path
from . import views

urlpatterns = [
    path('<int:survei_id>/', views.get_tracker_detail, name='tracker-detail'),
    path('<int:survei_id>/administrasi/', views.update_administrasi_status, name='update-administrasi'),
    path('<int:survei_id>/logistik/', views.update_logistik_status, name='update-logistik'),
    path('<int:survei_id>/pengendali-mutu/', views.update_pengendali_mutu_status, name='update-pengendali-mutu'),
]