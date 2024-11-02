from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("get-list-souvenir",get_list_souvenir),
    path("get-souvenir-detail/<str:id>/",get_souvenir_detail),
    path("add-souvenir/",add_souvenir),
    path("update-souvenir/<str:id>/",update_souvenir),
    path("delete-souvenir/<str:id>/",delete_souvenir),
]