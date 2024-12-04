from django.urls import path
from . import views

urlpatterns = [
    path('daftarDokumen/', views.dokumen_list, name='dokumen_list'),
    path('<path:id>/delete/', views.dokumen_delete, name='dokumen_delete'),
    path('searchDokumen/', views.search_dokumen, name='search_dokumen'),
    path('detailDokumen/<path:id>/', views.dokumen_detail, name='dokumen_detail'),
]
