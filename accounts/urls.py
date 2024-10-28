from django.urls import path
from . import views
from accounts.views import login_view
from accounts.views import profil_view
from accounts.views import get_security_question, check_role_eksekutif, check_role_administrasi, check_role_admin, check_role_logistik, check_role_pengendalimutu, check_role_proposal


urlpatterns = [
    path('api/login/', login_view, name="login"),
    path('api/get-security-question/', get_security_question, name='get_security_question'),
    path('api/profil/', profil_view, name='profil'),
    path('check_role_eksekutif/', check_role_eksekutif, name='check_role_eksekutif'),
    path('check_role_administrasi/', check_role_administrasi, name='check_role_administrasi'),
    path('check_role_admin/', check_role_admin, name='check_role_admin'),
    path('check_role_logistik/', check_role_logistik, name='check_role_logistik'),
    path('check_role_pengendalimutu/', check_role_pengendalimutu, name='check_role_pengendalimutu'),
    path('check_role_proposal/', check_role_proposal, name='check_role_proposal'),
]
