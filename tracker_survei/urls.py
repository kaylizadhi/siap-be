from django.urls import path
from .views import SurveyStatusView

urlpatterns = [
    path('<int:survey_id>/', SurveyStatusView.as_view(), name='survey-status')
]
