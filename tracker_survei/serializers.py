from rest_framework import serializers
from .models import Client, Survey, SurveyStatus

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']

class SurveySerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Survey
        fields = ['id', 'name', 'client']

class SurveyStatusSerializer(serializers.ModelSerializer):
    survey = SurveySerializer()

    class Meta:
        model = SurveyStatus
        fields = [
            'id', 'survey', 'invoice_sent', 'payment_received', 'dp_invoice_sent',
            'contract_signed', 'survey_questions_prepared', 'data_analysis_started',
            'final_administration_completed', 'report_delivered'
        ]
