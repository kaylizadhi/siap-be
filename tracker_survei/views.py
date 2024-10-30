from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SurveyStatus
from .serializers import SurveyStatusSerializer

class SurveyStatusView(APIView):
    def get(self, request, survey_id):
        try:
            survey_status = SurveyStatus.objects.get(survey__id=survey_id)
            serializer = SurveyStatusSerializer(survey_status)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SurveyStatus.DoesNotExist:
            return Response({"error": "Survey status not found"}, status=status.HTTP_404_NOT_FOUND)
