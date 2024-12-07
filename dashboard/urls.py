from django.urls import path
from .views import get_surveys_by_scope

urlpatterns = [
    path('survei/<str:scope>/', get_surveys_by_scope, name='dashboard_surveys_by_scope'),
]
