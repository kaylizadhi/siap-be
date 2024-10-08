from django.urls import path
from . import views

urlpatterns = [
    path('', views.klien_list, name='klien_list'),
    path('create/', views.klien_create, name='klien_create'),
    path('<int:id>/', views.klien_detail, name='klien_detail'),
    path('<int:id>/update/', views.klien_update, name='klien_update'),
    path('<int:id>/delete/', views.klien_delete, name='klien_delete'),
    path('search/', views.search_klien, name='search_klien'),
]
