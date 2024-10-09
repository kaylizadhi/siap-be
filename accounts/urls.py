from django.urls import path
from . import views
from accounts.views import login_view

urlpatterns = [
    path('api/login/', login_view, name="login"),
]
