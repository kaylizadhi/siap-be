from django.urls import path
from . import views
from accounts.views import login_view
from accounts.views import profil_view
from accounts.views import get_security_question
# verify_security_answer

urlpatterns = [
    path('api/login/', login_view, name="login"),
    path('api/get-security-question/', get_security_question, name='get_security_question'),
    # path('verify-security-answer/', verify_security_answer, name='verify_security_answer'),
    path('api/profil/', profil_view, name='profil'),
]
