"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, logout_view, dashboard_view, get_csrf_token, profil_view, get_security_question, verify_security_answer, change_password
from django.contrib.auth import views as auth_views
from tracker_survei.views import SurveyStatusView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buatAkun/', include('buatAkun.urls')),
    path('', include('example_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('accounts.urls')),
    path('api/get-security-question/', get_security_question, name='get_security_question'),
    path('api/verify-security-answer/', verify_security_answer, name='verify_security_answer'),
    path('api/change-password/', change_password, name='change_password'),
    path('api/profil/', profil_view, name="profil"),
    path('api/login/', login_view, name="login"),
    path('api/logout/', logout_view, name="logout"),
    path('api/dashboard/', dashboard_view, name="dashboard"),
    path('csrf/', get_csrf_token, name='get_csrf_token'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api/survei/',include('survei.urls')),
    path('klien/', include('klien.urls')),
    path('survey-status/', include('tracker_survei.urls')),
    path('dokumen_pendukung/', include('dokumen_pendukung.urls')),
]
