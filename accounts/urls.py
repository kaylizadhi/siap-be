from django.urls import path
from . import views
from accounts.views import login_view
from accounts.views import profil_view

urlpatterns = [
    path('api/login/', login_view, name="login"),
    # path('api/profil/', profil_view, name='profil'),
]
