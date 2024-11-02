from django.urls import path
from . import views

urlpatterns = [
    path('<int:survei_id>/', views.get_tracker_detail, name='tracker-detail'),
    path('<int:survei_id>/update/', views.update_tracker_status, name='tracker-update'),
]
